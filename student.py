students = []

def add_student(name):
    students.append(name)

add_student("John")
def display_students():
    for s in students:
        print(s)

display_students()