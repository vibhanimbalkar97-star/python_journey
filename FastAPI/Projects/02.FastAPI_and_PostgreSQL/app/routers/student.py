from fastapi import Path, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.student import StudentDB

router = APIRouter()
# Part 9: GET one student
#Depends(get_db) means: "Before running this endpoint, run the get_db() function and give me what it returns."

@router.get('/students/{student_id}')
def get_student(
    student_id : str = Path(..., description=f"The Id of the student", examples=["S001"]),
    db : Session = Depends(get_db)
):
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail=f"Student of id '{student_id}' not found"
        )
    return student
