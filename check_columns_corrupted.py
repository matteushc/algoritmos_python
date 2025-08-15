from pyspark.sql.functions import col, lit, count, when

customers_schema = '''
email STRING,
msisdn INT,
cupom_desconto STRING,
data_criacao_cupom TIMESTAMP,
data_expiracao_cupom TIMESTAMP,
fl_encarteirado STRING,
_corrupt_record STRING
'''

customers_df = spark.read.schema(customers_schema).format("csv").options(
    header=True,
    delimiter=";",
    mode="PERMISSIVE",
    columnNameOfCorruptRecord="_corrupt_record"
).load("C:\\Users\\F8086757\\Downloads\\file_input_1_20240123.csv")

from operator import or_
from functools import reduce

customers_df = customers_df.filter(col("_corrupt_record").isNotNull())

inspected = customers_df.columns
null_counts = customers_df.select([count(when(col(c).isNull(), c)).alias(
    c) for c in customers_df.columns]).first().asDict()

null_columns = [k for k, v in null_counts.items() if v > 0]
df = customers_df.drop(*null_columns)

customers_df.show()

customers_df.filter(col("_corrupt_record").isNull()).show()
