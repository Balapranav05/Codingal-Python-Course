class Student:
    __schoolName='XYZ School'

    def __init__(self,name,age):
        self.__name=name
    
    def __display(self):
        print("This is a private method")
    
std=Student("Bill", 25)
print(std.__schoolName)
