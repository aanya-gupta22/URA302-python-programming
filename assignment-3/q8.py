class StudentInfo:
    def student(self, name, age, course):
        print(f"Name: {name}, Age: {age}, Course: {course}")

    def display_argument_names(self):
    
        args = self.student.__code__.co_varnames[:self.student.__code__.co_argcount]
        print("Arguments of student function:", args)

info = StudentInfo()
info.student("Aanya", 19, "Robotics and AI")


