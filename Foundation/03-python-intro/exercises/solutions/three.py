class Student(Person):
    
    def __init__(self,name,age, gpa):
        super().__init__(name,age)
        self.gpa = gpa
        
    def info(self):
        return f"The student is called {self.name} and is {self.age} years old. He has a overall GPA of {self.gpa} at uni."