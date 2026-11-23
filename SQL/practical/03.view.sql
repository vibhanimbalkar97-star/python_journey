-- View 1: Available Fitness Products
create view available_fitness_products as
select p.product_id, p.name, p.price, p.stock_quantity
from products p
where p.category = 'Fitness' and p.is_available = True;

select * from available_fitness_products;

-- View 2: Low Stock Products
create view low_stock_products as
select p.name, p.category, p.stock_quantity
from products p
where p.stock_quantity < 30;

select * from low_stock_products;