list1 = [2,4,6,6,6,7,3,1]
list2 = ['c' , 'python' , 'c' , 'java' , 'cpp']

list1.pop()                             # remove the last
list1.append(5)                         # add at last
list1.remove(4)                         # remove specific element
list1.insert(10,12)                     # add at specific place
list1.sort()                            # Ascending order of list

print("List 1 : " , list1)
print("List 2 : " , list2)

print("First Element of List1 : " , list1[0])
print("Last Element of List1 : " , list1[-1])
print("List Slicing of List1 : " , list1[1:6])

list1.reverse()                         # Reverse the list
print("Reversed list1 : " , list1)

print("Maximum of list1 : " , max(list1))
print("Maximum of list2 : " , max(list2))

print("Minimum of list1 : " , min(list1))
print("Minimum of list2 : " , min(list2))

print("Length of list1 : " , len(list1)) # Number of elements are given of list1
print("Length of list2 : " , len(list2)) # Number of elements are given of list2

count1 = list1.count(6)
print("Count of 6 in list1 : " , count1) # Number of repeated elements are given of list1
count2 = list2.count('c')
print("Count of c in list2 : " , count2) # Number of repeated elements are given of list2
