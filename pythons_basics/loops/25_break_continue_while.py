#Python continue Statement returns the control to the beginning of the loop
#means the loop will simply skip the condition mentioned in continue

'''for i in 'cutiecurls':
    if i == 'c' or i == 's':
        continue
    print(i, end = "")'''

#Python break statement brings control out of the loop.
#means it will just take the condition value and finish the loop

'''for i in 'crlyduesigns':
 
    # break the loop as soon it sees 'l'
    # or 's'
    if i == 'u' or i == 'y':
        break
 
print('Current Letter :', i)'''


#while loop'''
'''While Loop is used to execute a block of statements repeatedly 
 until a given condition is satisfied. 
And when the condition becomes false,
the line immediately after the loop in the program is executed.'''

'''count = 0
while (count < 3):
    count = count + 1
    print("Hello aaina")'''
    
'''in above code we are starting the while with count value zero 
and giving it a terminating point if value of count goes above 3 
terminate the loop ALSO giving a condition where we are increasing count 
by one before every print executon'''

# program to check if list still
# contains any element
a = [1, 2, 3, 4, 5]
  
while a:
    print(a.pop())
print(a)

'''In the above example, we have run a while loop over a list 
that will run until there is an element present in the list.'''