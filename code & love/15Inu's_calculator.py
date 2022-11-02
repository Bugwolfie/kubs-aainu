print("Heya buddy! How you doing")
print("welcome to Inu's Calculator")
print("1.Press 1 for Addition")
print("2.Press 2 for Substraction")
print("3.Press 3 for Multiplication")
print("4.Press 4 for Division")

# user's choice
op = int(input("Enter Choice(1-4): "))

if op == 1:
    aainu = int(input("Enter first number:"))
    kubs = int(input("Enter second number:"))
    love = aainu+kubs
    print("Sum = ",love)
    print("Treat Aainu with a pizza now")

elif op == 2:
    aainu=int(input("Enter first number:"))
    kubs=int(input("Enter second number:"))
    hate = aainu-kubs
    print("Difference = ", hate)
    print("Praise Aainu's smile!!")

elif  op == 3:
    aainu=int(input("Enter first number:"))
    kubs=int(input("Enter second number:"))
    puchu = aainu*kubs
    print("Product = ", puchu)
    print("Clean Aainu's room!!")

elif op == 4:
    aainu=int(input("Enter first number:"))
    kubs=int(input("Enter second number:"))
    sad = aainu/kubs
    print("Quotient = ", sad)
    print("suno..... \n acha ab jao")
    
else:
    print("Are you stupoid? \ncant you choose dumbass?")