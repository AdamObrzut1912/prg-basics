# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.surname = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.surname = "Kowalski"
    student2.name = "Olivia"
    student2.age = 21
    student2.surname = "Nowak"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name} {student1.surname}, {student1.age} years old')
    print(f'{student2.name} {student2.surname}, {student2.age} years old')

if __name__ == "__main__":
    main()