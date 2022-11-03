# create a list
bru = [17, 28, 67, 96, 69]
print(bru[3])
# update an element
bru[3] = 36
print(bru)
# list slicing
wolf = ["doggu", 'pillu', 'raven', 'caty', 1728]
print(wolf[0:4])
print(wolf[0:])
print(wolf[5:0:-1]) #reverse order print except first element
print(wolf[5::-1])  #all lements in reverse order
print(wolf[5::-2])  #reverse skipping one element
print(wolf[0:6:2])  # skipping one element

wolfie = wolf.copy()
wolfie.append("43")
print(wolfie)
print(wolf)