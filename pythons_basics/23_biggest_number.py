n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1>n2:
    if n1>n3:
        print(n1, "is biggest")
    else:
        print(n3, "is biggest")  
elif n2>n3:
    print(n2, "is biggest")  
else:
    print(n3, "is biggest")
