import os
import sys
from pyspark.sql import SparkSession

# Set environment variables
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['HADOOP_HOME'] = os.path.abspath("hadoop")
os.environ['PATH'] += os.pathsep + os.path.join(os.environ['HADOOP_HOME'], 'bin')

def debug_spark():
    print(f"Python Executable: {sys.executable}")
    print("Initializing SparkSession with fault handler...")
    try:
        spark = SparkSession.builder \
            .appName("DebugSpark") \
            .master("local[*]") \
            .config("spark.python.worker.faulthandler.enabled", "true") \
            .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true") \
            .getOrCreate()
        
        print(f"SparkSession created. Version: {spark.version}")
        
        # Simple RDD test
        print("Running simple RDD count...")
        rdd = spark.sparkContext.parallelize([1, 2, 3])
        print(f"Count: {rdd.count()}")
        
        spark.stop()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_spark()
