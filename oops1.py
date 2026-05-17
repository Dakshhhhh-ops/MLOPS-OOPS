# initiate a class

class employee:
    #constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 101
        self.salary = 50000
        self.designation = "Software Engineer"
        print("attributes/data execution completed")

    
    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is traveling to {destination}")


#create an object/instance of employee class
sam=employee() 
#print(sam.salary)

# calling a method of the class
sam.travel("New York")

print(type(sam))

