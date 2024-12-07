import unittest
from pyspark.sql import SparkSession
from chispa import assert_df_equality
from simplepyetl.simple_dataframe_operations import split_first_last_name


class TestSimpleDataFrameOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = (
            SparkSession.builder.master("local[1]")
            .appName("unittest-pyspark-local-testing")
            .getOrCreate()
        )

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_split_first_last_name(self):
        data = [("John Doe",), ("Jane Smith",), ("Alice Johnson",)]
        df_input = self.spark.createDataFrame(data, ["name"])

        expected_data = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Johnson")]
        df_expected = self.spark.createDataFrame(
            expected_data, ["first_name", "last_name"]
        )

        df_result = split_first_last_name(df_input)

        # Showing the expected and result DataFrames for better understanding -- can be commented out
        print("Expected DataFrame:")
        df_expected.show()
        print("Result DataFrame:")
        df_result.show()

        assert_df_equality(df_result, df_expected, ignore_nullable=True)

    def test_that_will_fail(self):
        self.assertEqual(1, 2)


if __name__ == "__main__":
    unittest.main()
