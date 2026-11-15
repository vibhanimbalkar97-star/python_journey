from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

"""
HTTP Method:
1. GET -> to just show or display any message on the website or the page
or on the applicatioon.
"""

@app.get('/hello') #Endpoint -> where on the URL the below message must be displayed.
def greet():
    return {"Hello"}

#Helper Function 1.
def load_data():
    with open("./students.json", "r") as fs:
        return json.load(fs)

@app.get('/students')
def get_data():
    return load_data()

"""
PATH - PARAMETERS
student_id -> This is our Path Parameter.
Path(..., description="the id of the student", examples=["S001"]) -> we can add custom things like ... = mandatory. It shows in docs.
"""
@app.get("/students/{student_id}")
def get_id(student_id:str = Path(..., description="The Id of student", example=["S001"])):
    data = load_data()

    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail = f"Student with Id '{student_id}' not found"
        )
    return data[student_id]

"""
QUERY-PARAMETERS = filter and sort the list of students using values after the ? in the URL
http://127.0.0.1:8000/filter?course=Python

? -> after this our query is present
course=Python -> this is key-value pair
& = means 2 query joins and result comes on both basis.
query = sort, filter, search. paginate
"""
@app.get("/filter")
def filter_student(course:str=Query(None, description="Show student only in this course", example=["Python"])):
    data = load_data()

    if course is None:
       return data

    filtered = {} # S001 = Ararv sharma
    for student_id, info in data.items():
        if info["course"].lower() == course.lower():
            filtered[student_id] = info
        print(filtered)
    return filtered

"""
sort by and order
# http://127.0.0.1:8000/sort?sort_by=marks,age,name&order=asc,desc
"""

SORT_FIELDS = ["marks", "age", "name"]
SORT_ORDER  = ["asc", "desc"]
