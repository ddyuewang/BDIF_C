from pyspark.sql import SQLContext
from pyspark.sql.functions import col

sqlContext = SQLContext(sc)

# given an input string file, here has to be thru hadoop put -fs first
test_20 = sqlContext.read.json("tweets/yue_test.json")

test_200 = sqlContext.read.json("tweets/yue_test_200.json")


test_2000.registerTempTable("test_2000")
＃filter based on language
en_tweet = sqlContext.sql("SELECT * FROM test_2000 WHERE lang = 'en' AND test like "%apple%" ")     

## create the corrected version
sqlContext.sql("SELECT * FROM people WHERE lang = 'en' AND  text like '%not%'").show()

people.filter((people['lang'] == "en")|(people['lang'] == "fr"))
t1 = people.where(col("lang").isin({"en", "ja"}))

