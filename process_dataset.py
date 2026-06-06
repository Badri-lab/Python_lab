import time as t
from pyspark.sql import SparkSession, Column, Row
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, when, monotonically_increasing_id, max as spark_max
from typing import Dict, Tuple


def create_session() -> SparkSession:
    return SparkSession.builder \
        .appName("RetailDataAnalysis") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.2") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.hadoop.fs.s3a.access.key", "AKIAYMVP5KTIGPQZUA3E") \
        .config("spark.hadoop.fs.s3a.secret.key", "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") \
        .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
        .getOrCreate()


def build_bronze_layer(location: str, session: SparkSession) -> DataFrame:
    dataframe: DataFrame = session.read.csv(location, header=True, inferSchema=True)
    return dataframe.toDF(*[c.replace(' ', '_') for c in dataframe.columns])


def handle_duplicate_and_null(dataframe_in: DataFrame, session: SparkSession) -> DataFrame:
    dataframe_in.createOrReplaceTempView("o1")
    return session.sql("""
        SELECT Invoice, StockCode,
               COALESCE(Description, 'na') AS Description,
               Quantity, InvoiceDate, Price,
               CASE
                   WHEN Customer_ID IS NULL THEN
                       CASE
                           WHEN (Quantity < 0 AND Price = 0 AND Description IS NULL) THEN -1
                           WHEN (Quantity < 0 AND Price = 0 AND Description IS NOT NULL) THEN -2
                           WHEN (Quantity < 0 AND Price > 0) THEN -3
                           WHEN (Quantity > 0 AND Price = 0 AND Description IS NULL) THEN -4
                           WHEN (Quantity > 0 AND Price = 0 AND Description IS NOT NULL) THEN -5
                           WHEN (Quantity > 0 AND Price > 0) THEN -6
                           WHEN (Quantity > 0 AND Price < 0) THEN -7
                           ELSE 0
                       END
                   ELSE
                       Customer_ID
               END AS Customer_ID,
               Country
        FROM (
            SELECT DISTINCT Invoice, StockCode, Description, Quantity,
                            InvoiceDate, Price, Customer_ID, Country
            FROM (
                SELECT Invoice, StockCode, Description, Quantity,
                       InvoiceDate, Price, Customer_ID, Country,
                       ROW_NUMBER() OVER (
                           PARTITION BY Invoice, StockCode, Description, Quantity,
                                        Price, Customer_ID, Country
                           ORDER BY InvoiceDate DESC
                       ) AS rn
                FROM (
                    SELECT DISTINCT Invoice, StockCode, Description, Quantity,
                                    InvoiceDate, Price, Customer_ID, Country
                    FROM o1
                )
            )
            WHERE rn = 1
        )
    """)


def build_dimension(dataframe_in: DataFrame, *fields: Column) -> DataFrame:
    return dataframe_in.select(*fields).distinct()  # Select distinct rows based on the provided fields


def create_control_table(session: SparkSession, dimensions_to_process: Dict[str, Tuple[str, str]]) -> DataFrame:
    control_data = [Row(Dimension=dimension_name, LastProcessedKey=-1) for dimension_name in dimensions_to_process]
    return session.createDataFrame(control_data)


def add_surrogate_key_with_control(dimension_dataframe_in: DataFrame, dimension_key_name: str,
                                   control_table: DataFrame, dimension_name: str) -> Tuple[DataFrame, DataFrame]:
    last_processed_key = \
        control_table.filter(col("Dimension") == dimension_name).select("LastProcessedKey").collect()[0][0]
    if dimension_key_name in dimension_dataframe_in.columns:
        df_filtered = dimension_dataframe_in.filter(col(dimension_key_name) > last_processed_key)
    else:
        df_with_key = dimension_dataframe_in.withColumn(dimension_key_name, monotonically_increasing_id())
        df_filtered = df_with_key.filter(col(dimension_key_name) > last_processed_key)

    df_with_key = df_filtered.withColumn(dimension_key_name, monotonically_increasing_id())

    new_last_processed_key = df_with_key.agg(spark_max(dimension_key_name)).collect()[0][0]
    updated_control_table = control_table.withColumn("LastProcessedKey",
                                                     when(col("Dimension") == dimension_name,
                                                          new_last_processed_key)
                                                     .otherwise(col("LastProcessedKey")))
    return df_with_key, updated_control_table


def iterate_dimensions_with_control(dataframe_in: DataFrame, dimensions_to_process: Dict[str, Tuple[str, str]],
                                    control_table: DataFrame) -> Tuple[Dict[str, DataFrame], DataFrame]:
    dimension_dataframes: Dict[str, DataFrame] = {}
    for dimension_name, fields in dimensions_to_process.items():
        # Common function for loading Dimensions
        dimension_df = build_dimension(dataframe_in, *[col(f) for f in fields])
        # Surrogate Key to be loaded after the data load using  Common Function
        dimension_df_with_key, control_table = add_surrogate_key_with_control(
            dimension_df, f"{dimension_name}Key", control_table, dimension_name)
        dimension_dataframes[dimension_name] = dimension_df_with_key
    return dimension_dataframes, control_table


def build_golden_layer(dataframe_in: DataFrame,
                       dim_dfs: Dict[str, DataFrame],
                       dim_key_fields_map: Dict[str, Tuple[str, str]]) -> DataFrame:
    dataframe_out: DataFrame = dataframe_in
    for dimension_name, (key_field, additional_field) in dim_key_fields_map.items():
        df_dimension = dim_dfs[dimension_name]
        selected_columns = [key_field, f"{dimension_name}Key", additional_field]
        dataframe_out = dataframe_out.join(df_dimension.select(*selected_columns), on=[key_field, additional_field],
                                           how="left")
    fact_columns = ["Invoice", "StockKey", "Quantity", "InvoiceDate", "Price", "CustomerCountryKey"]
    dataframe_out = dataframe_out.select(*fact_columns)
    return dataframe_out


def process_dataset(session: SparkSession, file_location: str = "s3a://myawsbucket-20240820/online_retail_II.csv") -> None:
    def show_df_sampledata(num_rows: int = 5):
        tn = t.time()
        print('bronze layer count: ', df_bronze_layer.count())
        df_bronze_layer.show(num_rows, truncate=0)
        print('silver layer count: ', df_silver_layer.count())
        df_silver_layer.show(num_rows, truncate=0)
        print('control table: ', df_control_table.count())
        df_control_table.show(num_rows, truncate=0)
        print('CustomerCountry dimension count: ', df_customer_dimension.count())
        df_customer_dimension.show(num_rows, truncate=0)
        print('Stock dimension count: ', df_stock_dimension.count())
        df_stock_dimension.show(num_rows, truncate=0)
        print('golden layer count: ', df_golden_layer.count())
        df_golden_layer.show(num_rows, truncate=0)
        print(f'show_df_sampledata() for {file_location} took {round(t.time() - tn)} seconds.')

    tx = t.time()
    print(f'Starting to process dataset {file_location}...')
    # Raw data load to create BRONZE layer using dataset from Kaggle - STAGE DATA
    df_bronze_layer: DataFrame = build_bronze_layer(file_location, session)
    # SILVER layer creation by cleansing and transformation of the data in BRONZE layer
    df_silver_layer: DataFrame = handle_duplicate_and_null(df_bronze_layer, session)
    dimension_to_key_field_map: Dict[str, Tuple[str, str]] = {"CustomerCountry": ("Customer_ID", "Country"),
                                                              "Stock": ("StockCode", "Description")}
    # Control table creation using dimensions and their respective fields chosen from the SILVER layer dataset
    df_control_table: DataFrame = create_control_table(session, dimension_to_key_field_map)
    # Iterative dimension loads using the control table
    dimension_dfs, df_control_table = iterate_dimensions_with_control(df_silver_layer, dimension_to_key_field_map,
                                                                      df_control_table)
    df_customer_dimension: DataFrame = dimension_dfs.get(list(dimension_to_key_field_map.keys())[0])
    df_stock_dimension: DataFrame = dimension_dfs.get(list(dimension_to_key_field_map.keys())[1])
    # GOLDEN layer creation by joining Dimensions to Silver layer
    df_golden_layer: DataFrame = build_golden_layer(df_silver_layer, dimension_dfs, dimension_to_key_field_map)
    show_df_sampledata(4)
    print(f'{file_location} processing took {round(t.time() - tx)} seconds.')


spark: SparkSession = create_session()
spark.sparkContext.setLogLevel("ERROR")
# process_dataset(spark)
print('SCD Type1 - scenario implementation and testing')
process_dataset(spark, "s3a://myawsbucket-20240820/online_retail_II_v1.csv")
process_dataset(spark, "s3a://myawsbucket-20240820/online_retail_II_v2.csv")
