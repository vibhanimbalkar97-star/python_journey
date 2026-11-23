-- Stored Procedure
-- Add Product Procedure

create procedure add_product(
p_name varchar,
p_sku char(8),
p_price numeric,
p_qty int,
p_category text
)
language plpgsql
as $$
Begin
     insert into products(name, sku_code, price, stock_quantity, category)
	 values(p_name, p_sku, p_price, p_qty, p_category);
	 raise notice 'Product added successfully';
end;
$$;

call add_product('Bottle', 'AB123456', 2000, 30, 'Fitness');

select * from products;