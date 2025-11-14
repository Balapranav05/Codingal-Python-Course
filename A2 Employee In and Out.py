#Create class
class Employee:

    def __init__(self):
        print("Employee created")

    def __def__(self):
        print("Destructor called")

def Create_obj():
    print("Making Object ...")
    obj=Employee()
    print("Function End ...")
    return obj

print("Calling Create_obj() function ...")
obj=Create_obj
print("Program End ...")