#single inheritance 
class Parent:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello ,my name is {self.name}")
        
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")
        
#create an instance of child
child=Child("Pasam Tharun")
child.greet()
child.play()
        
        
#Multilevel Inheritance
class Grandparent:
    def __init__(self,name):
        self.name=name
    def tell_story(self):
        print(f"{self.name} is telling the story")

#intermediate class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working")

#derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is Playing ")
        
#create an instance of child 
child=Child("Pasam Tharun")
child.tell_story()
child.work()
child.play()


#herarchical inheritance 
class Parent:
    def __init__(self,name):
        self.name =name 
    def greet(self):
        print(f"Hello,my name is {self.name}")
        
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing football")
        
class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying")
        
#create an instance of the child1 and child2
child1=Child1("pasam")
child2=Child2("Tharun")
child1.greet()
child1.play()
child2.greet()
child2.study()


#Multiple inheritance
#base class
class A:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello From A,{self.name}")
        
#intermediate class1
class B(A):
    def greet(self):
        print(f"Hello from B,{self.name}")
        super().greet()
        
#intermediate class2       
class C(A):
    def greet(self):
        print(f"Hello From C,{self.name}")
        super().greet()
        
#derived class       
class D(B,C):
    def greet(self):
        print(f"Hello from D,{self.name}")
        super().greet()
        
#create an instance of D
d=D("Chinna")
d.greet()

#Hybrid Inheritance
#base class
class Animal():
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        print(f"{self.name} makes a sound")

#intermediate class1(Hierarchical) 
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

#intermediate class2 (Multilevel)      
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

#derived class (multiple inheritance)
class Bat(Mammal,Bird):
    def __init__(self,name):
        Mammal.__init__(self,name)
        
    def nocturnal(self):
        print(f"{self.name} is nocturnal")

#create an instance of Bat
bat=Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()
print(Bat.mro())
