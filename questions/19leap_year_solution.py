#solution leap year
year = int(input("enter the year to check =  "))
if year%100 == 0:
    if year%400 == 0:
        print("Hell yeah! \n its a leap year")
    else:
        ("nahi hai buddy leap year")

else:
    if year%4 == 0:
        print("you got it buddy \n its a leap year")
    else:
        print("sorli not a leap year sweetu")
