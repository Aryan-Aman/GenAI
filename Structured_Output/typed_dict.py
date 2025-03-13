from typing import TypedDict

class Person(TypedDict):
    name: str
    age : int

man : Person = {"name":"AMAN" , "age": "infinite"}#age : 23 or "infinite" no error >{'name': 'AMAN', 'age': 'infinite'}
print(man)