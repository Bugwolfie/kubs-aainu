#what are loops
'''1. loops helps to execute a statement or group of statements
   as many times as you want

   2. there are some conditions which are set to enter a loop 
   and then certain conditions for desired execution

   3. as soon as the conditions become false the loop will stop execution
  '''
  #For Loop in Python

''' For loops are used for sequential traversal.
 For example: traversing a list or string or array etc.
  In Python, there is no C style for loop, i.e., for (i=0; i<n; i++).
   There is “for in” loop which is similar to "for 
   each" loop in other languages. Let us learn how to use for
    in loop for sequential traversals.'''


    #loop for tables
'''table = int(input("enter the number you want table for = "))
print("table of", table , "is")

for i in range(1, 11):
    result = table*i

    print(table,"X",i,"=",result)'''

#loop for Aaina
'''for i in "aainasharma":
    print(i)'''

#loop for reversed Aaina
curls = input("enter the string to check = ")

opp = ""
for i in range(len(curls)-1, -1, -1):
    aaina = opp+curls[i]
if aaina == curls:
    print("yes")
else:
    print("not")
    
    


#loop for all even numbers till 10
'''for i in range(1,11,2):
    print(i)'''


#how to use a counter
'''count = 0
for vowels in "aayanshisharma" :
    if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
        count = count+1
print(count)'''


'''aaina = 1
for vowels in "aayanshisharma" :
    pass
print(aaina)'''
