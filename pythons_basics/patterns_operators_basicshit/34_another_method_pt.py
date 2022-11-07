def star(n):
    for i in range(0, n+1, 1):
        print(" "*i, end= "  ")
        print()
star(6)

def star2(n1):
    for i in range(0,n1,1):
        print("*"*(n1-i), end= "  ")
        print()

star2(5)
