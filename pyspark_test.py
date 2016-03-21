# Load the proper libary - the main function used here is pyspark and its SQLContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import col

sqlContext = SQLContext(sc)

# given an input string file, here has to be thru hadoop put -fs first, the need to source the hadoop directory
test_20 = sqlContext.read.json("tweets/yue_test.json")
# test_200 = sqlContext.read.json("tweets/yue_test_200.json")

# register the TempTable for later usage - serve like a table
test_20.registerTempTable("test_20")

### data scrubbing

# filter based on language
en_tweet = sqlContext.sql("SELECT * FROM test_20 WHERE lang = 'en'")
en_tweet.registerTempTable("en_tweet")

# filter based on keywords search
apple_en_tweet = sqlCOntext.sql("SELECT * FROM test_20 WHERE text like '%apple%' or text like '%Apple%' or like 'macbook' or like ")


## create the corrected version
sqlContext.sql("SELECT * FROM people WHERE lang = 'en' AND  text like '%not%'").show()

people.filter((people['lang'] == "en")|(people['lang'] == "fr"))
t1 = people.where(col("lang").isin({"en", "ja"}))

