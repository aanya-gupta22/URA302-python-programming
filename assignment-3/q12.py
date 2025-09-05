class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None 

    def set_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)


student = Student(1024230089, "Aanya")
student.set_class("2W14")
student.display_attributes()
