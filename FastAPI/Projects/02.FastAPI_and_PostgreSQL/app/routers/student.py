from fastapi import Path, Depends, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.student import StudentDB
from app.schemas.student import StudentResponse, StudentCreate, StudentUpdate
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func




router = APIRouter()
# Part 9: GET one student
#Depends(get_db) means: "Before running this endpoint, run the get_db() function and give me what it returns."
# tags = group the same routes means get all routes in Get.

@router.get('/students/{student_id}', response_model=StudentResponse, tags=["GET ROUTES"])
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
@router.post('/CreateStudent', response_model=StudentResponse, status_code=201, tags=["POST ROUTES"])
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
        db.rollback()   #Cancels everything the session did since the last commit()
        raise HTTPException(
            status_code=400,
            detail=f"Email '{student.email}' is already used by another student"
        )
    db.refresh(new_student)
    return new_student

# Part 11: PUT - update a student
@router.put('/UpdateStudent/{student_id}', tags=["PUT ROUTES"])
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
        db.rollback()   #Cancels everything the session did since the last commit()
        raise HTTPException(status_code=400, detail=f"Email '{student.email}' is already used by another student")

    db.refresh(student)
    return student

# Part 12: DELETE - remove a student
@router.delete('/DeleteStudent/{student_id}', tags=["DELETE ROUTES"])
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

# Part 13: GET all students (filter + sort + paginate)

SORT_FIELDS = ["marks", "age", "name"]
SORT_ORDER  = ["asc", "desc"]

@router.get('/students', tags=["GET ROUTES"])
def get_all(
    course : str  | None = Query(None, description="show only students in this course", examples=["Python"]),
    sort_by: str  | None = Query(None, description="Sort by marks, name, age"),
    order  : str         = Query("asc", description="asc or desc", examples=["desc"]),
    page   : int         = Query(1, ge=1, description="Which page you want (starts from 1)"),
    limit  : int         = Query(2, gt=1, le=100, description="How many students you want one page (1 to 100)"),
    db: Session = Depends(get_db)
):
    if sort_by is not None and sort_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort_by '{sort_by}', Choose from {SORT_FIELDS}"
        )

    if order not in SORT_ORDER:
        raise HTTPException(
                    status_code=400,
                    detail=f"Invalid order '{order}', Choose from {SORT_ORDER}"
        )

    query = db.query(StudentDB) #SELECT * FROM student_records

    if course:                  #WHERE -> SELECT * FROM student_records WHERE course == "Python";
        query = query.filter(func.lower(StudentDB.course) == course)

    total_students = query.count()

    if sort_by:
        column = getattr(StudentDB, sort_by) #"marks" -> StudentDB.marks

        if order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    else:
        query = query.order_by(StudentDB.id)

    start = (page - 1) * limit
    students   = query.offset(start).limit(limit).all() # end

    return {
        "page": page,
        "limit":limit,
        "total_students": total_students,
        "students": students
    }