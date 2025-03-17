from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# class Student(BaseModel):
#     name : str

# new_stud = {"name":32}

# student = Student(**new_stud)
# print (student)

####################################################### Basic Example #################################################
# class Student(BaseModel):
#     name :str ="aman"

# new_stud ={}
# student = Student(**new_stud)
# print(student)  # Output: Default name="aman" if no arg is passed

################################################## Set Default Values #################################################

# class Student(BaseModel):
#     name: str = "aman"
#     age : Optional[int] = None

# new_stud ={'age':'23'}
# student = Student(**new_stud)
# print(student) #> name='aman' age=None(if no age passed) ; name='aman' age=23 (age passed) ;[ name='aman' age=23 ( even if passed as '23'>string ) -> this is type coercing in python pydantic self analyzes what is passed ]

############################################ Optional fields, Coerce ##################################################

# class Student(BaseModel):
#     name: str = "aman"
#     age : Optional[int] = None
#     email : EmailStr

# new_stud ={'age':'23', 'email':'abc'} #'abc' will give error , while 'abc@gmail.com' will not
# student = Student(**new_stud)
# print(student)

#######################################Built-In Validation ############################################################

class Student(BaseModel):
    name: str = "aman"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10.1, default=5, description='A decimal value representing cgpa') #can add constraints ,also can add default values


new_stud ={'age':'23', 'email':'abc@gmail.com'} #'abc' will give error , while 'abc@gmail.com' will not ; if(cgpa not passed) default =5 
student = Student(**new_stud) #pydantic object, but can convert to python dict or json
student_dict=dict(student)
student_json=student.model_dump_json()
print(student_dict) #> {'name': 'aman', 'age': 23, 'email
print(student_json) #> {"name": "aman", "age": 23, "email
print(student)


