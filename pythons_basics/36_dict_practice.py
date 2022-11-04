limb = [1,1,1,1,1,2,2,4,3,3,3,3,3,5,5,5,3,3,4,2,4,1,3,1,3]
disco= {}


#writing a python program to add this 
#list's original elements to a dict and their occurances as the values

for i in limb:
    if i not in disco:
        disco[i]=1
    else:
        disco[i] +=1

print(disco)

#writing a python program to check which key has maximum value
limbo = []
for i in disco.keys():
    limbo.append(disco[i])

max = limbo[0]

for i in limbo:
    if max>i:
        continue
    else:
        max = i
print(max)

for i in disco.keys():
    if disco[i]<max:
        continue
    else:
        disco[i]=max
print(i, "has highest occurances which is", max)