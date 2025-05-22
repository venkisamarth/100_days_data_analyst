# strings in python are surrounde by eiter single quotation marks, or double quotation marks

# you can display a string literal with the print function 
print("Hello")
print('Hello')

# quotes inside quotes
print("It's alright")
print("he is called 'jonny")
print("he is calle  'jonny")

# assign string to varaile 
# assigning a string to variable is done with the varaible name followed by an equal sign and the string  

a="Hello"
print(a)

# multiline strings 

a="""" Lorem ipsum dolor sit amet this 
this is the text geneated form the html lorem"""

print(a)

# or three single quote 
a=''' this is one of the main dngarous from the 
creating the main problem in the separate'''


# String  are arrays 

# like many other porgramming language string in python are of bytes represting uncode character  

a="Hello, world"
print(a[1])

# lopping thorigh the string  

for x in a: 
    print(x)

# string lenght 
a="venkatesh j mariyappanver"
print(len(a))

a="hello world"
print(len(a))

# check string 
text="this is the one type of string"
print(isinstance(text,str))



print("this " in text)


# use it in and if statemtn

# example

txt="The best things in life are free!"
if "free!" in txt: 
    print("yes,'free' is presnt ")

# check if not
# check if expensive is not present in the following text 
txt='The best things in life are free!'
print("Expensive " not in txt)

# use it in and if statment 
txt ="the best things in life arefree"

if "expresive" not in txt:
    print(" No, 'expensive' is NOT present")
    

