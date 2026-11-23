--  One-to-Many: Products & Orders. 

create table products(
product_id int primary key,
product_name varchar(50),
category text,
price numeric(10,2),
stock_quantity int,
is_available boolean,
added_on date
);

create table orders(
order_id int primary key,
product_id int,
quantity int,
order_date date,
customer_name varchar(50),
paymen_method varchar(50),
constraint fk_product
    foreign key (product_id)
	references products(product_id)
	on delete cascade
);

-- Q1. Show each order along with the product name and price
SELECT o.order_id, o.customer_name, p.product_name, p.price
FROM orders o
JOIN products p 
ON o.product_id = p.product_id;

-- Q2. Show all products even if they were never ordered
select p.product_name, o.order_id
from products p left join orders o
on p.product_id = o.product_id;

-- Q3. Show orders for only 'Electronics' category
select o.order_id, p.product_name, p.category
from orders o join products p
on o.product_id = p.product_id
where p.category = 'Electronics';

-- Q4. List all orders sorted by product price (high to low)
select o.order_id, p.product_name, p.price
from orders o join products p
on o.product_id = p.product_id
order by p.price desc;

-- Q5. Show number of orders placed for each product
select count(o.order_id) as total, p.product_name
from orders o right join products p
on o.product_id = p.product_id
group by p.product_name;

-- Q6. Show total revenue earned per product
select p.product_name, sum(o.quantity * p.price) as revenue
from products p join orders o
on o.product_id = p.product_id
group by p.product_name order by revenue asc;

-- Q7. Show products where total order revenue > ₹2000
select p.product_name, sum(o.quantity * p.price) as revenue
from products p join orders o
on o.product_id = p.product_id
group by p.product_name 
having sum(o.quantity * p.price) > 2000;

-- Q8. Show unique customers who ordered 'Fitness' products
select distinct o.customer_name, p.category
from orders o join products p
on o.product_id = p.product_id
where p.category = 'Fitness';

select * from products;
select * from orders;

