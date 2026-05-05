# Average Salaries
# https://platform.stratascratch.com/coding/9917-average-salaries?code_type=6

# Import your libraries
import pyspark
from pyspark.sql.functions import col, avg
from pyspark.sql.window import Window
# Start writing code

window = Window.partitionBy('department')
employee = employee.withColumn('avg_salary', avg('salary').over(window)).orderBy('department').select('department','first_name','salary','avg_salary')

# To validate your solution, convert your final pySpark df to a pandas df
employee.toPandas()



# Find all posts which were reacted to with a heart
# https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=6

from pyspark.sql.functions import col

df = facebook_posts.alias("p").join(facebook_reactions.alias("r"), on="post_id", how="inner").filter(col("r.reaction") == "heart").select("p.*").distinct()

df.toPandas()


