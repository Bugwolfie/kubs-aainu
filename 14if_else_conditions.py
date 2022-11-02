# so now its time to put a little logic in our codes
# if else elif conditionals in python are some 
# basic terms and conditions for performing tasks
# we simply tell python if certain condition satisfy 
# the requirements do this operation otherwise/else treat it differently
# there can be one or many conditions applied for the task
'''The following are the conditional statements provided by Python. 

1. if
2. if..else
3. Nested if
4. if-elif statements.'''



'''if condition:           
    Statements to execute if
    condition is true  '''
   #for example
   #1 if condition
'''kubs = 27
if kubs == 27:
    print("kubs is a good number")'''

#if else
'''kubs = input("please enter name")
if kubs == "aainu":
    print("kubs is a good name")
else:
    print("bakwas name")'''

#nested if
'''a = int(input("enter a number"))
if a <= 12:
    if a > 0:
        print("a is not yours")
    else:
        print("kya bolna chah rha hai")    
else:
    print("a is totally yours") '''

#if elif statements
aaina = input("enter aaina's details =  ") 
if aaina == "charu":
    print("maaji's choice")
elif aaina == "paridha":
    print("chaujee's choice") 
elif aaina == "inu":
    print("zomato's choice") 
elif aaina == "mirku":
    print("koi bolke dikhaye")
elif aaina == "bebu":
    print("kubs favourite")
else:
    print("aaina is a hungry")
         
        