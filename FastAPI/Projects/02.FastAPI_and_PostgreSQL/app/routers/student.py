from fastapi import Path, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.student import StudentDB
from app.schemas.student import StudentResponse, StudentCreate, StudentUpdate
from sqlalchemy.exc import IntegrityError


router = APIRouter()
# Part 9: GET one student
#Depends(get_db) means: "Before running this endpoint, run the get_db() function and give me what it returns."

@router.get('/students/{student_id}', response_model=StudentResponse)
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

# Part 10: POST - create a student
@router.post('/CreateStudent', response_model=StudentResponse, status_code=201)
def create_student(student : StudentCreate, db : Session = Depends(get_db)):
    if db.get(StudentDB, student.id):
        raise HTTPException(
            status_code=404,
            detail=f"Student with the Id '{student.id}' already exists"
        )
    new_student = StudentDB(**student.model_dump())
    db.add(new_student)

    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail=f"Email '{student.email}' is already used by another student"
        )
    db.refresh(new_student)
    return new_student

# Part 11: PUT - update a student
@router.put('/UpdateStudent/{student_id}')
def update_student(student_update : StudentUpdate, 
                   student_id : str = Path(..., description="The Id of the student", examples=["S001"]),
                    db : Session = Depends(get_db)):
    
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail=f"The student with id '{student_id}' not found"
        )

    changes = student_update.model_dump(exclude_unset=True)

    for key, value in changes.items():
        setattr(student, key, value)

    try:
        db.commit()
        
    except IntegrityError:
        raise HTTPException(status_code=400, detail=f"Email '{student.email}' is already used by another student")

    db.refresh(student)
    return student

# Part 12: DELETE - remove a student
@router.delete('/DeleteStudent/{student_id}')
def delete_student(student_id : str = Path(..., description="The Id of the student", examples=["S001"]),
                       db: Session = Depends(get_db)):
    student = db.get(StudentDB, student_id)

    if student is None:
        raise HTTPException(
                        status_code=404,
                        detail=f"The student with id '{student_id}' not found"
                    )
    db.delete(student)
    db.commit()

    return {"message": f"Student '{student_id}' deleted successfully"}
  