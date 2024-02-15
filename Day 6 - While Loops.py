#DEFINING AND CALLING PYTHON FUNCTIONS
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#In Python a function is defined using the def keyword
#Make sure to indent the code inside the function
#Create a function
def my_function():
  print("Hello")
  print("Bye")

#Call the function
#To call a function, use the function name followed by parenthesis
my_function()


#WHILE LOOPS
#The while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
#While a condition is true, the loop will continue to execute the block of code.
#The condition is tested at the beginning of the loop.
#If the condition is false, the loop ends and the program continues to the next line.
#The while loop requires relevant variables to be ready, in this example we need to define an index that we'll use to count the number of times the loop has executed.
#The index is commonly called i for "iteration"

#Example:
#For loop
for item in list_of_items:
  #Do something to each item
for number in range(a,b):
  print(number)

#While loop
while something_is_true:
  #Do this
  #Then do this
  #Then do this

