# Part 5: Pydantic schemas for input (StudentCreate, StudentUpdate)

from pydantic import BaseModel, Field, EmailStr, field_validator,ConfigDict, computed_field

class StudentCreate(BaseModel):
    id     : str  = Field(..., examples=["S001"])
    name   : str  = Field(..., min_length=2, max_length=50)
    age    : int  = Field(..., gt=0 , le=100 )
    course : str  = Field(..., max_length=50)
    marks  : int  = Field(..., ge=0  , le=100)
    email  : EmailStr

@field_validator("name")
@classmethod
def check_name(cls, value):
    if not value.replace(" ", "").isalpha():
        return ValueError(f"Name must contain only space and letters")
    return value.title()

class StudentUpdate(BaseModel):
    id     : str | None  = Field(None, examples=["S001"])
    name   : str | None  = Field(None, min_length=2, max_length=50)
    age    : int | None  = Field(None, gt=0 , le=100 )
    course : str | None  = Field(None, max_length=50)
    marks  : int | None  = Field(None, ge=0  , le=100)
    email  : EmailStr | None = None
    
    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value.replace(" ", "").isalpha():
            return ValueError(f"Name must contain only space and letters")
        return value.title()

# Part 6: Pydantic schemas for output (StudentResponse, StudentPage, Message)
#from_attributes=True lets Pydantic read student.marks (an object), not only student["marks"]
class StudentResponse(StudentCreate):
    model_config = ConfigDict(from_attributes=True)

    @computed_field
    @property
    def grade(self) -> str:
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