from pyspark.pandas import DataFrame


def df_cols_null_check(df: DataFrame):
    for col_name in df.columns:
        c = df.filter(df[col_name].isNull()).count()
        if c:
            print(col_name)