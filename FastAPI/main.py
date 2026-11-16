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

@app.get("/sort")
def sort_data(sort_by : str = Query(None, description="Sort by marks, name, age",
    examples=["marks"]),
    order : str = Query("asc", description="asc or desc", examples=["asc", "desc"])):

    #If the given sort_by input dosn't belongs to any (marks, age, name) we will raise an error.
    if sort_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid sort_by {sort_by}, choose from {SORT_FIELDS}"
        )
    #If the given order input dosn't belongs to any (asc, desc) we will raise an error.
    if order not in SORT_ORDER:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid order '{order}. Choose from {SORT_ORDER}"
        )
    
    data = load_data()

    #step-1 Turn the dictionary into a list, putting the ID inside each student
    student = []
    for student_id, info in data.items():
        info['id'] = student_id 
        student.append(info)

     #Step-2 Sort the list by the choosen field
    reverse = (order == "desc")
    sorted_students = sorted(student, key = lambda s:s[sort_by], reverse=reverse)
    print(sorted_students)
    return sorted_students

"""
PAGINATION
http://127.0.0.1:8000/paginate?page=1&limit=2

page -> which page you want
limit -> how many students(records) on one page

Formula:
start = (page - 1) * limit
end = start + limit
page start from 1 not 0 = by default in query parameter 1.
page always greater than 0 and non -ve value. 
limit threshold means set the limit betn 2 t0 100

"""
@app.get("/paginate")
def paginate_student(page : int = Query(1, ge=1, description="Which page you want (start from 1)"),
                     limit: int = Query(2, ge=1, le=100, description="How many students on one page (1 to 100)")):

    data = load_data()

    student = []
    for student_id, info in data.items():
        info['id'] = student_id
        student.append(info)

        start = (page -1 ) * limit
        end   = start + limit

        page_student = student[start : end]

        total_student = len(student)

    return {
        "page"         : page,
        "limit"        : limit,
        "page_student" : page_student,
        "total_student": total_student
    }