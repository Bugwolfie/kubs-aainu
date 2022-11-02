# list methods
# listname.sort()  it sorts a list in ascending order
# listname.reverse()   reverse the given list (the order of elements)
# listname.append(data)  add an element value in the list at last position
# listname.insert(index, data) add the new element at desired index
# listname.pop(index) pop the data from the mentioned index from the list
# listname.pop() pop the data from the last index from the list
# listname.remove(data) remove the mentioned element from the list
# listname.count(data)
# listname.extend(another list name)
# listname.clear()  removes all the elements from the list

wolf_list = [1,34,17, 3456, 17, -14, 365, 2, 78, 0]
wolf_list.sort()
print(wolf_list)
wolf_list.reverse()
print(wolf_list)
wolf_list.append(999)
print(wolf_list)
wolf_list.insert(1, 143)
print(wolf_list)
wolf_list.pop(1)
print(wolf_list)
wolf_list.remove(17)
print(wolf_list)
wolf_list.pop()
print(wolf_list)
wolf_list.pop()
print(wolf_list)
fake_wolf = ["mayra", 17, 60, 2002]
wolf_list.extend(fake_wolf)
print(wolf_list)
aa = wolf_list.count("mayra")
print(aa)
fake_wolf.clear()
print(fake_wolf)