
# creation of class
class classer:

    # creation of variables which we call them as attributes

    a = 34
    b = "hi this is b"

    # creation of constructer
    # constructer will be called for every time a new object is created
    # constructors are used to initialize the instance varible
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    # this is called as function
    # we have to manually call the methods

    # self is a default variable which is always pointing to the
    # the currebt object (like this keyword in the java)
    # by using the self keyword we can access the instance
    # variable and methods of the object
    def func(self):
        # we will put the self in the method parameters
        # if we have of usage of particular objects
        # arguments in the method
        print("this is argument1 and argument2 " +
              self.parameter1+self.parameter2)

# creation of object


obj1 = classer("1arg1", "1arg2")
obj2 = classer("2arg1", "2arg2")

# calling of methods
# we can call the methods in two types

# 1st type of calling the methods we are passing the object name in the paranthesis
# classer.func(obj1)
# classer.func(obj2)

# 2nd type of calling of methods
# in this type we will pass the object as
# like the above type but it is all done innnerly
obj1.func()
obj2.func()

print(obj1.a)
