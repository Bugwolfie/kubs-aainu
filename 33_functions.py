from random import randint
#python function
'''
Python Functions is a block of statements that return the specific task.

The idea is to put some commonly or repeatedly done tasks together 
and make a function so that instead of writing the same code again and again
for different inputs, we can do the function calls to reuse code contained
in it over and over again. 
  '''
print()
type(23)

# why we use functions
'''
1. to reduce duplicacy in code
2. to make our code easy to understand
3. helps  in wrapping our code in small boxes(modularity)


'''
#example1
'''def aaina():
  print("hello")
  print("welcome to the class")
  print("you will be assigned a roll no. and id card soon!")
  print("Aaina is your CR")
  print("Aaina is the most beautiful human")
  print("she will take attendences too")

#1000*1= 1000lines

def odder(n):
  """it is a function to check if the number is even or odd"""
  if n %2 != 0:
    return("odd like you")
  else:
    return("not odd")
n1 = int(input("enter here = "))
res = odder(n1)
print(res)
#ret = odd(24)
#print(ret)
print(odder.__doc__)

 def evenodd(n):
  i = 1
  while i>0:
    n = int(input("enter number here = "))
    if n%2 == 0:
        return("its even")
    else:
        return("its odd like you")

print(evenodd(25)) 
print(randint.__doc__)'''


'''def sum_of_cubes():
  n = int(input("enter the till u want sum of cubes= "))
  s = 0
  for i in range(1,n+1):
    s = s+i**3
  print(s)
sum_of_cubes()'''

#the inputs in functions are called parametrs 
# and output is called return values

''' suppose i have to write a function with input values(a,b)
 and output or return value as (a+b)
 '''
def add(a,b):
  s = a+b
  return s
#return does not print anything 
add(345,7890)
#thats how we can make it print
print(add(5,7890))
"if we dont provide return to the function it will return None"
#see
def add1(a,b):
  s = a+b

print(add1(3,6))