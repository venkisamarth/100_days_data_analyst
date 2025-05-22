# python goble varaible
# globle varaibles

# varaibles that are created outside of the function (as in all ofthe example in the prevois ) are know as  globle  variable

# example  
x="awsome"
def my_func(): 
    print("python is "+ x)
my_func()

# create the varaible inside a function, with the same name as the goble varaible
def my_func():
    x="fantastic"
    print('python is a  '+  x+"  language")
my_func()

print("python is  "+x)


# The goble keyword

# normally when you create a  vraible inside a funcion that variable is local and can only used inside the function

# To create a globle varaible inside a function you can use the globle keyword

# example 

# if you use the globel keyword the varaible belongs to the globle scope

def myfunc():
    global x
    x="fantastic"

myfunc()

print("python is "+x)
# also  use the global keword if you want to change a globle valriable inside a funciton 
# example 

x="awesome"

def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is "+x)