# python numbers 

# int , float ,complex

# varaible of numaric types are created when you assign a alue to them

x=1 
y=2.8
z=1j
print(x,y,z)

# to verify the types of any object in python use the type() function in pytho
print(type(x))
print(type(y))
print(type(z))

# int type in python

# int or interger  is a whole ,positive or negative , without decimals of unlited leng
# example

x=1
y=344545656
z=-3434
print(type(x))
print(type(y))
print(type(z))


# float  
# float or floating point numbers is a number , positive  or negative , containg  one or more decimal 

print(type(x))
print(type(y))
print(type(z))

x=1.22
y=1.4
z=-343.3
print(type(x))
print(type(z))
print(type(x))
print(type(z))

# complex 
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

# type conversion in python  

# example

x=1 
y=2.5
z=1j

# convert  from one type to another  

a=float(x)
# convert from flaot into int 
b=int(y)

# convert  from int to complext 

c=complex(x)

print(type(a))
print(type(b))
print(type(c))


print(type(a))
print(type(b))
print(type(c))


# Randome numbers

# python does not have a random() function to maek randome numbers , but python have builtin  module called random that can be usd to make  randome numbers 

# exmaple  
import random
print(random.randrange(1,10))