n = int(input("enter the number you want factorial of=  "))
fact = 1
for i in range(n,1,-1):
    fact = fact*i
print("factorial of" , n, "is", fact)

#we can use the range this way too
n = int(input("enter the number you want factorial of=  "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("factorial of" , n, "is", fact)

#we can do it with nested for loop too
n = int(input("enter the number you want factorial of=  "))
fact = 0
for i in range(1,n+1):
    for j in range(1,2):
        res = i*j
    fact = fact+res
print("factorial of" , n, "is", fact)
