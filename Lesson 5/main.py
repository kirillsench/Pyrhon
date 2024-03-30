import requests
#1 help().
#help(requests)

'''
r = requests.get('https://www.python.org')
print(r.status_code)
print(b'Python is a programming language' in r.content)

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

'''
print(requests.__name__)
print(type(requests.Response()))
print(dir(requests.Response))
'''

#has atrr get attr

'''
print(hasattr(requests.Response, 'content'))
print(getattr(requests.Response, 'content', 'object has no attribute "content1"'))
'''

#callable
'''
def show(show:str):
    print(name)
name = "Andrii"



print(callable(show))
print(callable(name))
'''


#5 issubclass

'''
class Human:
    pass
class Student(Human):
    pass

class Teacher:
    pass

student = Student()
print(issubclass(Student, Human))#True
print(issubclass(Teacher, Human))#False
print(isinstance(student, Human))#True
print(isinstance(student, Student))#True
print(isinstance(student, Teacher))#False

'''
