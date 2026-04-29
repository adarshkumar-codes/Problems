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


