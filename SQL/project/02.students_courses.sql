-- Many-to-Many: Students & Courses

-- Tables & Sample Data

create table students(
student_id int primary key,
student_name varchar(50)
);

create table courses(
course_id int primary key,
course_name varchar(50)
);

insert into students
values (1, 'Karan'),
       (2, 'Tejaswini'),
	   (3, 'Isha');

insert into courses
values (101, 'Python'),
       (102, 'React'),
	   (103, 'JS');

select * from students;
select * from courses;
select * from students_courses;

create table students_courses(
student_id int,
course_id int,
primary key(student_id, course_id),
FOREIGN key (student_id) references students(student_id),
FOREIGN key (course_id) references courses(course_id)
);

-- Sample Mapping
insert into students_courses
values(1,101), (1,102), (2, 102), (2,103), (3,101), (3,102)

-- Queries
-- Q1. Show student and course names
select s.student_name, c.course_name
from students_courses sc
join students s on sc.student_id = s.student_id
join courses c on sc.course_id = c.course_id;

-- Q2. List all courses taken by 'Tejaswini'
select s.student_name, c.course_name
from students_courses sc
join students s on sc.student_id = s.student_id
join courses c on sc.course_id = c.course_id
where s.student_name = 'Tejaswini';