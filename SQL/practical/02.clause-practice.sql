create table products(
product_id serial primary key,
name varchar(50) not null,
sku_code char(8) unique not null,
price numeric(10,2) check(price >= 0),
stock_quantity int default 0 check(stock_quantity >= 0),
is_available boolean default TRUE,
category text not null,
added_on date default current_date,
last_update Timestamp default now()
);

INSERT INTO products (name, sku_code, price , stock_quantity, is_available, category)
VALUES
('Wireless Mouse', 'WM123456', 699.99, 50, TRUE, 'Electronics'),
('Bluetooth Speaker', 'BS234567', 1499.00, 30, TRUE, 'Electronics'),
('Laptop Stand', 'LS345678', 799.50, 20, TRUE, 'Accessories'),
('USB-C Hub', 'UC456789', 1299.99, 15, TRUE, 'Accessories'),
('Notebook', 'NB567890', 99.99, 100, TRUE, 'Stationery'),
('Pen Set', 'PS678901', 199.00, 200, TRUE, 'Stationery'),
('Coffee Mug', 'CM789012', 299.00, 75, TRUE, 'Home & Kitchen'),
('LED Desk Lamp', 'DL890123', 899.00, 40, TRUE, 'Home & Kitchen'),
('Yoga Mat', 'YM901234', 499.00, 25, TRUE, 'Fitness'),
('Water Bottle', 'WB012345', 349.00, 60, TRUE, 'Fitness');

select * from products;

-- Test 1 clause
-- show name and price of all
select name, price from products;

-- Show all products where the category is 'Electronics'.
select * from products where category = 'Electronics';

-- Group products by category. Show each category once.
select category from products group by category

-- Show categories that have more than 1 product.
select category, count(*) from products
group by category
having count(*) > 1;

-- Show all products sorted by price in ascending order.
select * from products order by price;

-- Show only the first 3 products from the table.
select * from products limit 3;

--  Show product name as "Item_Name" and price as "Item_Price".
select name as Item_Name, price as Item_price from products;

-- Show all the unique categories from the products table.
select distinct category from products;

-- Test 2 clause + operators + aggregate fun
-- Display the name and price of the cheapest product in the entire table.
select name, price from products 
where price = (select min(price) from products);

-- Find the average price of products that belong to 'Home & Kitchen' or 'Fitness'.
select round(avg(price), 2) from products 
where category in ('Home & Kitchen', 'Fitness');

-- Show product names and stock quantity where product is available, stock > 50, and price != 299.
select name, stock_quantity from products 
where is_available = True 
and stock_quantity > 50 
and price !=299;

-- Find the most expensive product in each category.
select category, max(price) from products group by category;

-- Show all unique categories in uppercase, sorted in descending order.
select distinct upper(category) as category_upper 
from products 
order by category desc;

select name,
case
    when is_available then 'in_stock'
	else 'out_stock'
end as avability_status
from products;

select name, stock_quantity,
case 
     when stock_quantity > 100 then 'high stock'
	 when stock_quantity between 30 AND 100 then 'medium stock'
	 else 'low stock'
end as label
from products;


select * from products;

select * from products;