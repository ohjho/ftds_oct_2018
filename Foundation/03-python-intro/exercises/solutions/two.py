class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"The person is called {self.name} an is {self.age} years old"