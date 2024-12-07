from pyspark.sql import functions as F
from pyspark.sql import DataFrame


def split_first_last_name(df_input: DataFrame) -> DataFrame:
    """Split a column into first and last name.

    Args:
        df_input (DataFrame): Input DataFrame with a column "name".

    Returns:
        DataFrame: Output DataFrame with two columns "first_name" and "last_name".
    """
    output_col = (
        df_input.withColumn("first_name", F.split(df_input["name"], " ")[0])
        .withColumn("last_name", F.split(df_input["name"], " ")[1])
        .drop("name")
    )

    return output_col
