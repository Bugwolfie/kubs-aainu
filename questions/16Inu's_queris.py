#intersection, symmetric diff, union
# addition of two sets
from xml.dom.expatbuilder import theDOMImplementation


set1 = {1,2,3,4,5,6,7}
set2 = {14,15}
set3 = set2.intersection(set1)
print(set3)

set4 = set1.union(set2)
print(set4)
set5 = set1.symmetric_difference(set2)
print(set5)
set6 = set1.isdisjoint(set2)
print(set6)

#well about "in" and "not in" 
'''they are basically operators 
which harry hasnt covered in those videos yet 
idk why he used them

back to the point

there are many kind of operators in python like assignment operator,
arithmatical operators, logical operators and many more

these "in" and "not in" are membership operators

they are used to check if that given item is a member of
  targeted list, set, tuple, string or dictionary.

we can check for any datatype whether its a string, float or integer

special note: in dictionary we cant use these operators to check values
   so they can be used to check membership of keys only" '''

paridha_list = [12, 14, 567, 34, 45, 87]
print(18 in paridha_list)
check = 12 not in paridha_list
print(check)

''' if you can see above in line 39 and 40 i used 
them with two different ways
once directly printing the result and once using a 
variable to get and print the result'''