# variables

# thee are 3 types of variables right there

# 1.instance
# 2.static
# 3.local

# 1.instance  mostly based upon the reference variable

# declaration

# inside a constructor using a self keyword
# self.c=5
# inside a isinstance method using a self keyword
# self.c=5
# out side of a class using a objects reference variable
# t=class_name()
# t.d=40

# access
# inside the class by using the self keyword
# print(self.a)
# and outside the class by using a objectreference variable
# t1=class_name()
# print(t1.a)

# 2.static variable mostly based upon class name

# declare

# if the value of the variable is not varied from the object
# to object then we call it as a static variable
# we can call this in the constructor ,instance method
# and static method by using simply the class name
# we declare the static variable in the class method by using
# either a class name or a object reference variable

# access

# we can accesss

# by using the self or classname if it is in the
# either instance or constructor

# inside the static method by using a class name

# inside a class method by using a either class name or class variable

# outside of the class by using a either class name or class variable


# 3.local variable

# local varible is a temperory requirement particularly
# for the specific method ,after the method the local or
# temperory variable will be destroyed

# we can not access the local variable outside of the
# particular method for which the variable had been created
