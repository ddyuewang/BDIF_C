mport os
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
APP_NAME = "My Spark Application"
if __name__=="__main__":
  conf = SparkConf().setAppName(APP_NAME)
  conf = conf.setMaster("local[*]")
  sc = SparkContext(conf=conf)
  sqlContext = SQLContext(sc)
  df = sqlContext.read.json("./59.json")
  df1=sc.parallelize(df.take(10))
  df1.saveAsTextFile("tweets3/hahahah.txt")
