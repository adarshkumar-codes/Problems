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
