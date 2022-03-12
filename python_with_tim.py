# Output and printing
print('Hello World!')

#float
print(4.5, "Hello") 

# this means go to the next line after this line is
print("Hello", 'end', 87, False, end='\n')
print("Hello")

# this means it does NOT go to the next line
print("Hello", 'end', 87, False, end='|')
print("Hello")


# VARIABLES

hello = 'tim'
world = 'world'
world = hello
hello = 'no'

print(hello, world)

# hello_world is the convention
# 9hello is a no go 
# hello 9 also doesn't work

# INPUT

# name = input('Name: ')
# age = input('Age: ')
# print('Hello', name, 'you are', age, 'years old')

# ARITHMETIC OPERATORS
# Use INT when you don't want it to be a float
# x = 9
# y = 3.5
# result = int(x / y)  
# # x ** y this is an exponent
# print(result)

# num = input('Number: ') -> str
# taking whatever they input and print out the number minus 5
# print(num - 5)
# THIS PRODUCE ERROR B/C ITS READING IT AS A STRING

# num = input('Number: ')
# # print(int(num) - 5)
# print(float(num) - 5)


# STRING METHODS
# Puts everything in the upper case
# hello = 'hello'.upper()
# print(hello)

# hello = 'hello'
# print(hello.upper())

# hello = 'hello'
# print(hello.lower())

# Put the first letter of the entire string, so it is two words, only the first one capitalizes 
# .capitalize() 

# count the specific string within a strong and see how many time that occurs
hello = 'heLLO World'
print(hello.count('11'))
# none shows up because it is looked for 2 lowercase l's back to back and we only have capitals there

hello = 'heLLO World'
print(hello.lower().count('ll'))
# shows one b/c there is one now

hello = 'heLLO World'
print(hello.lower().count('o'))

# CONDITIONAL OPERATORS




