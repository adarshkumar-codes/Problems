# MacBookPro User Event Count
# https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=2
import pandas as pd
playbook_events = playbook_events[playbook_events['device'] == 'macbook pro']
playbook_events = playbook_events.groupby('event_name', as_index = False).agg(event_count=('device', 'count')).sort_values('event_count',ascending=False)
# Start writing code
playbook_events.head(len(playbook_events))


# Inspection For Glassell Coffee Shop
# https://platform.stratascratch.com/coding/9689-inspection-for-glassell-coffee-shop?code_type=2
import pandas as pd
los_angels_restaurant_health_inspections = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['owner_name']=='GLASSELL COFFEE SHOP LLC']
los_angeles_restaurant_health_inspections.head()


# Hour Of Highest Gas Expense
# https://platform.stratascratch.com/coding/10005-hour-of-highest-gas-expense?code_type=2
# Import your libraries
import pandas as pd
lyft_rides = lyft_rides[lyft_rides['gasoline_cost'] == lyft_rides['gasoline_cost'].max() ][['hour']]
# Start writing code
lyft_rides.head()


# Finding Updated Records
# https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2
# Import your libraries
import pandas as pd

ms_employee_salary = ms_employee_salary[
ms_employee_salary['salary'] == ms_employee_salary.groupby('id')['salary'].transform('max')]
# Start writing code
ms_employee_salary.head(76)


# 2877. Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/description/
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id','age'])


# 1327. List the Products Ordered in a Period
# https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[
    (orders['order_date'].dt.month == 2) &
    (orders['order_date'].dt.year == 2020)]
    orders = orders.groupby('product_id', as_index=False).agg({'unit': 'sum'})
    orders = orders[orders['unit']>=100]
    orders = orders.merge(products, on='product_id', how='inner')
    return orders[['product_name','unit']]
    

# 185. Department Top Three Salaries
# https://leetcode.com/problems/department-top-three-salaries

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')
    employee['rank'] = employee.groupby('name_y')['salary'].rank(method='dense', ascending=False)
    employee = employee[employee['rank']<4]
    return pd.DataFrame({'Department':employee['name_y'], 'Employee':employee['name_x'], 'Salary':employee['salary']})


# 175. Combine Two Tables
# https://leetcode.com/problems/combine-two-tables/

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person = pd.merge(person, address, on='personId', how='left')
    return person[['firstName','lastName','city','state']]


# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, left_on = 'managerId', right_on='id', how='left')
    employee = employee[employee['salary_x']>employee['salary_y']]
    return pd.DataFrame({'Employee':employee['name_x']})


# 182. Duplicate Emails
# https://leetcode.com/problems/duplicate-emails/

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person['is_it'] = person['email'].duplicated()
    person = person[person['is_it']==True]
    return pd.DataFrame({'Email':person['email'].unique()})


# 178. Rank Scores
# https://leetcode.com/problems/rank-scores/

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score','rank']].sort_values('score', ascending=False)
