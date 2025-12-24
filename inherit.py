##base case
#what get inherited --constructors,non private methods and attributes 
#class animal:
#    def __init__(self,name):
#        self.name=name
#    
#    def speak(self):
#        print(f"{self.name} makes a sound")
#
##derived class
#class dog(animal):
#    def speak1(self):
#        print(f"{self.name} barks")
#        
##creating an istamce of animal class
#Animal=animal("Generic Animal")
#Animal.speak() #OUTPUT: Generic Animal makes a sound
#
##creating the instance for dog class
#Dog=dog("buddy")
#Dog.speak()  #OUTPUT: buddy makes a sound


#Super keyword
#base class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")
        
#derived class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__("Dog") #calling the base class constructor
        self.breed=breed
    def speak(self):
        super().speak()  #calling the base class method
        print(f"{self.name} barks.it is a {self.breed}")

#creating an instance of Dog class
dog=Dog("German Shepherd")
dog.speak()

#MRO (Method Resolution Order)
print(Animal.mro())
        
