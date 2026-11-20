-- create table
CREATE TABLE Students(
id INT,
name CHAR(50),
age INT,
grade CHAR(1)
)

-- insert values
INSERT INTO Students(name, age, grade)
VALUES ('ABC', 44, 'A+')

-- update values
Update Students
set age = 45
where name='ABC';

-- delete values
delete from Students
where age = 40;

-- read specific column
select name from Students

-- read values
SELECT * FROM Students


