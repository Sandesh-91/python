#as in c++ we have parameterized constructor in python we use __init__ method

# _str_ is used to define the human readable representation  string of an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(abc):
        return f"Person(name={abc.name}, age={abc.age})"

p = Person("Alice", 25)#here p is an object of class Person()
print(p)  # automatically calls p.__str__()

#delete object properties
del p.age 

#delete whole object
del p



class Person1:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person1("Sandesh", 20)
p1.myfunc() 