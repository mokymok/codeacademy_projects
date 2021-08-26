-- 1
-- What are the column names?
select*from orders limit 10;

-- 2 
-- How recent is this data?
select distinct(order_date) from orders order by 1 desc;

-- 3
-- Instead of selecting all the columns using *, 
-- write a query that selects only the special_instructions column.

-- Limit the result to 20 rows.
select special_instructions from orders limit 20;

-- 4 
-- Can you edit the query so that we are only 
-- returning the special instructions that are not empty?
select special_instructions from orders where special_instructions is not null limit 20;

-- 5
-- Let’s go even further and sort the instructions 
-- in alphabetical order (A-Z).
select special_instructions from orders where special_instructions is not null order by 1 asc limit 20;

-- 6
-- Let’s search for special instructions that have the word ‘sauce’.
-- Are there any funny or interesting ones? 
select special_instructions from orders where special_instructions is not null and special_instructions like '%sauce%'order by 1 asc limit 20;
--"SRIRACHA SAUCE"

-- 7
-- Let’s search for special instructions that have the word ‘door’.
-- Any funny or interesting ones?
select special_instructions from orders where special_instructions is not null and special_instructions like '%door%'order by 1 asc limit 20;
--"super hungover. let yourself in pass the fridge turn left and double doors my bedroom. im in my pajamas watching james bond 1love"

-- 8
-- Let’s search for special instructions that have the word ‘box’.
-- Any funny or interesting ones?
select special_instructions from orders where special_instructions is not null and special_instructions like '%box%'order by 1 asc limit 20;
--"Cleanse yourself with the sage in the mailbox."

-- 9
-- Instead of just returning the special instructions, also return their order ids.
-- For more readability:
-- Rename id as ‘#’
-- Rename special_instructions as ‘Notes’
select id as'#',special_instructions as'Notes' from orders where special_instructions is not null and special_instructions like '%box%'or special_instructions like '%door%' or special_instructions like '%sauce%'order by 1 asc limit 20;

-- 10
-- Challenge
-- They have asked you to query the customer who made the phrase. 
-- Return the item_name restaurant_id, and user_id for the person created the phrase.
select user_id as 'User',item_name as'Item',restaurant_id as 'Store',id as'#',special_instructions as'Notes' from orders where special_instructions is not null and special_instructions like '%box%'or special_instructions like '%door%' or special_instructions like '%sauce%'order by 1 asc limit 20;
