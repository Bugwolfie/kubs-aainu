# a starry square
'''n = int(input("how many Inu you want in each side of your starredsquare =  "))
for i in range(n):
    for j in range(n):
        print("Inu", end = "")
    print("\n")
   

 # a starred increasing triangle
n = int(input("max A you want in your increasing triangle  =  "))
for i in range(n):
    for j in range(i+1):
        print("AK", end = " ")
    print()

# a starred decreasing triangle
n = int(input("max AK you want in your decreasing triangle  =  "))
for i in range(n):
    for j in range(i,n):
        print("AK", end = " ")
    print()'''


#right sided traingle
n = int(input("max * you want in your rightsided triangle  =  "))
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end= " ")
    print()

#right  sided downward traingle
n = int(input("how many $ you want in your traingle = "))

for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n):
        print("$", end= " ")
    print()

#pyramid shape 
n= int(input("enter here ^ you want in pyramid's edges = "))

for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("^", end = " ")  
    for j in range(i+1):
        print("^", end=" ")
    print()  

# reverse pyramid shape 
n= int(input("enter here ^ you want in ulta pyramid's edges = "))
for i in range(n):   
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("^", end = " ")
    for j in range(i,n-1):
        print("^", end=" ")    
    print()


#for diomond shape
n= int(input("enter here ^ you want in diomond's edges = "))

for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("^", end = " ")  
    for j in range(i):
        print("^", end=" ")
    print()  
for i in range(n):   
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("^", end = " ")
    for j in range(i,n-1):
        print("^", end=" ")    
    print()