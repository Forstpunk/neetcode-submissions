-- Write your query below
select s.name from sales_person s where s.sales_id not in (
    select o.sales_id from orders o join company c on o.com_id = c.com_id where c.name ='CRIMSON'
)