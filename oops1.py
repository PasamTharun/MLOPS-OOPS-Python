#initiate a class
class employee:
    #special megthod/magic method/dunder method---constructor(all the data/atributes are automatically called as soon as we are created the obj)
    def __init__(self):
        print("started executing the data/attributes")
        self.id=124
        self.salary=50000
        self.designation="SDE"
        print("attributes/data are initiated/completed")
        
    def travel(self,destination):
        print("this travel method is manually called")
        print(f"the employee is travelling to {destination}")

#creating a obj /instance of a class
pasam=employee()

#print(pasam.id)
pasam.travel("bangalore")

    