-- Write your query below
select employee_id,
        CASE 
        when employee_id % 2 =1 and name not like 'M%'  Then salary
        else 0
        end as bonus from employees
        order by employee_id