-- 607. Sales Person
--   https://leetcode.com/problems/sales-person/description/
select name
from salesperson
where sales_id not in (
    select o.sales_id
    from orders o
    join company c on o.com_id = c.com_id
    where c.name = 'red'
);

-- Person's average > Average of the country, Problem from w3schools
select 
  s.CustomerName, 
  s.Country, round(s.average_p,2) as AverageByCountry, 
  round(t.average,2) as AverageByCustomer 
  from (
  SELECT 
  c.Country, 
  c.CustomerName, 
  avg(od.Quantity) as average_p 
  FROM Customers c 
  join Orders o 
  on c.CustomerID = o.CustomerID 
  join OrderDetails od 
  on od.OrderID = o.OrderID 
  group by c.CustomerName) s 
  left join (
  SELECT 
  c.Country, 
  avg(od.Quantity) as average 
  FROM Customers c 
  join Orders o 
  on c.CustomerID = o.CustomerID 
  join OrderDetails od 
  on od.OrderID = o.OrderID 
  group by c.Country) t 
  on s.Country = t.Country 
  where s.average_p > t.average;

-- 511. Game Play Analysis I
-- https://leetcode.com/problems/game-play-analysis-i/description/
select player_id, 
min(event_date) as first_login 
from Activity 
group by player_id

-- 176. Second Highest Salary
-- Solved
-- https://leetcode.com/problems/second-highest-salary/
select (select distinct salary from employee order by salary desc limit 1 offset 1) as SecondHighestSalary


-- 1661. Average Time of Process per Machine
-- Solved
-- https://leetcode.com/problems/average-time-of-process-per-machine/description/

select a.machine_id, round(avg(b.timestamp - a.timestamp),3) as processing_time from Activity a join Activity b
on a.machine_id = b.machine_id and a.process_id = b.process_id and a.activity_type = 'start' and b.activity_type = 'end'
group by a.machine_id


-- 1193. Monthly Transactions I
-- Solved
-- https://leetcode.com/problems/monthly-transactions-i/

select date_format(trans_date, '%Y-%m') as month, country, count(state) as trans_count, count(case when state='approved' then 1 end) as approved_count, sum(amount) as trans_total_amount, sum(case when state = 'approved' then amount else 0 end) as approved_total_amount from Transactions group by country, month;



-- 184. Department Highest Salary
-- Solved
-- https://leetcode.com/problems/department-highest-salary/description/

with total as (select d.name as Department, e.name as Employee, e.salary as Salary, rank() over(partition by d.name order by e.salary desc) as ranking from Employee e join Department d on e.departmentId = d.id)
select Department, Employee, Salary from total where ranking = 1
