# """
# PYDANTIC FUNDAMENTALS'

# mac :- pip3 install pydantic
# win :- pip install pydantic
# """

# """
# STEP 1 - The Problem
# A normal dictionary accepts ANYTHING. Nobody checks the data.
# """
# bad_student = {
#     "name" : "",
#     "age"  : "twenty",
#     "marks": "150",
#     "email": "email-123"
# }
# # print(bad_student) # it prints all data with invalid values
# #{'name': '', 'age': 'twenty', 'marks': '150', 'email': 'email-123'}

# """
# Step 2 - BASEMODEL + TYPE HINTS
# we describe a student ONCE. Python checks every student against it.
# """
from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field

# # class Student(BaseModel):
# #     name   : str
# #     age    : int
# #     marks  : int
# # s = Student(name="ABC", age="twenty", marks="150")
# # print(s.name, s.age, s.marks)
# # s.age gives an error = Input should be a valid integer, unable to parse string as an integer
# # s.marks = convert inside string number 150 to int. Needs number to convert. like age not allowed

# """
# Step 3 - FIELD() RULES
# gt = greater than               lt = less than
# ge = greater or equal           le = less or equal
# """
# class RuleStudent(BaseModel):
#     name    : str = Field(..., min_length=2, max_length=50)     #... = required
#     age     : int = Field(..., gt=0, lt=100)                    #1 to 99
#     marks   : int = Field(..., gt=0, le=100)                    #0 to 100
#     course  : str = "Python"                                    #default value -> Python
#     phone   : str | None = None                                 #Optional field can be empty

# # s = RuleStudent(name="Rohan Verma", age=21, marks=77)
# # print(s.name, s.age, s.marks, s.course, s.phone)
# #Rohan Verma 21 77 Python None

# """
# Step 4 - EMAILSTR
# checks the text really looks like an email.
# """
# class EmailStudent(BaseModel):
#     name : str
#     email : EmailStr

# # s = EmailStudent(name="Kabir Singh", email="kabirsingh@gmail.com")
# # print(s.name, s.email)

"""
Step 5 - FINAL STUDENT MODEL
1. field_validator  -> our OWN custom rule.
2. computed_field   -> a value Pydantic calculates for US.
"""
class Student(BaseModel):
    id    : str      = Field(..., examples=["S001"])
    name  : str      = Field(..., min_length=2, max_length=50)
    age   : int      = Field(..., gt=0, lt=100)
    email : EmailStr 
    course: str      = Field(..., max_length=50 )
    marks : int      = Field(..., ge=0, le=100)

    #Custom Rule : Name must contain only letters and spaces
    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and space")

        return value.title()  #first letter capital

# s = Student(id="S002", name="a b", age=20, email="abc@gmail.com", course="python", marks=99)
# print(s.id, s.name, s.age, s.email,s.course, s.marks)


    @computed_field
    @property
    def check_grade(self)->str:
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
        
s = Student(id="S001",
            name="aarav sharma",
            age = 21,
            course = "Python",
            marks=99,
            email="arav@gmail.com")
# print(s.id, s.name, s.age, s.email,s.course, s.marks, s.check_grade)


"""
Step 6 MODEL_DUMP()
turn a model back into Python dictionary (so that we can save it later)
object into dict bcz we cannot save the object, and s.student is a object.
convert object to dict.
post = when take input from user to save in db
"""
data = s.model_dump()
# print(data)



"""
Step 7 - CHECK OUR REAL DATA (students.json)
Every student in our file will go through the Student Model
"""
import json
with open("./students.json", "r") as fs:
    raw = json.load(fs)

for student_id, info in raw.items():
    s = Student(id=student_id, **info)
    print(s.id, s.name, s.course)