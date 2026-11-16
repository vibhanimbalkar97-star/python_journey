from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("./students.json", "r") as fs:
        return json.load(fs)

@app.get('/student')
def get_students(): 
    return load_data()

@app.get('/filter')
def filtered(course):
    data = load_data()

    if course is None:
        return data

    filtered = {}
    for student_id, info in data.items():
        if info["course"] == course:
            filtered[student_id] = info
        print(filtered)
    return filtered