# Most Profitable Financial Company
# https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=6
import pyspark
df = forbes_global_2010_2014.orderBy('profits', ascending=False).select('company','continent').limit(1)
df.toPandas()


# Find all Lyft rides which happened on rainy days before noon
# https://platform.stratascratch.com/coding/10004-find-all-lyft-rides-which-happened-on-rainy-days-before-noon?code_type=6
# Import your libraries
import pyspark
from pyspark.sql.functions import col
# Start writing code
lyft_rides = lyft_rides.filter((lyft_rides['weather'] == 'rainy') & (col('hour').between(0,11)))
# To validate your solution, convert your final pySpark df to a pandas df
lyft_rides.toPandas()


# Calculate Samantha's and Lisa's total sales revenue
# https://platform.stratascratch.com/coding/10127-calculate-samanthas-and-lisas-total-sales-revenue?code_type=6
# Import your libraries
import pyspark
from pyspark.sql.functions import col, sum
# Start writing code
sales_performance = sales_performance.filter((col('salesperson') == 'Samantha') | (col('salesperson') == 'Lisa'))
sales_performance = sales_performance.agg({'sales_revenue':'sum'})
# To validate your solution, convert your final pySpark df to a pandas df
sales_performance.toPandas()


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


