#to print it as it is
'''for i in "aaina":
    print(i,end="")'''

#for sum of a list
'''curls = [23,34,45678,45,76,69,23]

sum = 0
for i in curls:
    sum = sum+i
print(sum)'''

#more complex sum of list inputed by user
n = int(input("how many numbers you want in list = "))
curls = []
for i in range(n):
    curls.append(int(input()))

sum = 0
for i in curls:
    sum = sum+i
print(curls)
print(sum)
