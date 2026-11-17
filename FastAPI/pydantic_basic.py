"""
PYDANTIC FUNDAMENTALS'

mac :- pip3 install pydantic
win :- pip install pydantic
"""

"""
STEP 1 - The Problem
A normal dictionary accepts ANYTHING. Nobody checks the data.
"""
bad_student = {
    "name" : "",
    "age"  : "twenty",
    "marks": "150",
    "email": "email-123"
}
# print(bad_student) # it prints all data with invalid values
#{'name': '', 'age': 'twenty', 'marks': '150', 'email': 'email-123'}

"""
Step 2 - BASEMODEL + TYPE HINTS
we describe a student ONCE. Python checks every student against it.
"""
from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name   : str
    age    : int
    marks  : int
# s = Student(name="ABC", age="twenty", marks="150")
# print(s.name, s.age, s.marks)
# s.age gives an error = Input should be a valid integer, unable to parse string as an integer
# s.marks = convert inside string number 150 to int. Needs number to convert. like age not allowed

"""
Step 3 - FIELD() RULES
gt = greater than               lt = less than
ge = greater or equal           le = less or equal
"""
class RuleStudent(BaseModel):
    name    : str = Field(..., min_length=2, max_length=50)     #... = required
    age     : int = Field(..., gt=0, lt=100)                    #1 to 99
    marks   : int = Field(..., gt=0, le=100)                    #0 to 100
    course  : str = "Python"                                    #default value -> Python
    phone   : str | None = None                                 #Optional field can be empty

# s = RuleStudent(name="Rohan Verma", age=21, marks=77)
# print(s.name, s.age, s.marks, s.course, s.phone)
#Rohan Verma 21 77 Python None

"""
Step 4 - EMAILSTR
checks the text really looks like an email.
"""
class EmailStudent(BaseModel):
    name : str
    email : EmailStr

s = EmailStudent(name="Kabir Singh", email="kabirsingh@gmail.com")
print(s.name, s.email)
