from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def write_csv(df, path):
    df.write.csv(path, header=True)


def filter_csv(df, column, value):
    return df.filter(F.col(column) == value)


def show(df):
    df.show()


class PysparkModule:
    def __init__(self):
        self.spark = SparkSession.builder.appName("PysparkModule").getOrCreate()

    def read_csv(self, path):
        return self.spark.read.csv(path, header=True, inferSchema=True)

    def stop(self):
        self.spark.stop()