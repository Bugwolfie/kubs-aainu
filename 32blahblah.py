'''def number(n1,n2):
    for i in range(n1,n2+1):
        print(i)

n1 = 2
n2 = 20   
print(number(n1,n2))

n = (input(" yha daal = "))
for i in n:
    for j in range(1,11):
        print(int(i)*j)'''


#using while loop
n=5
 
i=1
j=0
''' while loop check the condition until the
 condition become false. if it is true then
 enter in to loop and print the pattern'''
'''while(i<=n):
    while(j<=i-1):
        print("* ",end="")
        j=j+1
     
    print()
    j=0
    i=i+1


#using list 
n= 5
myList = []
for i in range(1,n+1):
        myList.append("* "*i)
print("\n".join(myList))
from functions import sum_of_cubes
sum_of_cubes()'''

for i in range(6):
    for j in range(7):
        if (i==0 and j%3 !=0) or (i==1 and j%3 ==0) or (i-j==2) or (i+j==8):
            print("InU", end = "  ")
        else:
            print(" ", end = "   ")
    print("    ")