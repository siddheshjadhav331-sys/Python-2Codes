A = {3,4,5,6}
B = {5,6,7,8}

print("Set 1 elements : ")
for x in A:
    print(x , end=" ")
print()

print("Set 2 elements : ")
for y in B:
    print(y , end=" ")
print()

union_set = A | B
print("Union of A and B : " , union_set)

intersection_set = A & B
print("Intersection of A and B : " , intersection_set)

difference_set1 = A - B
print("Difference of Set(A - B) : " , difference_set1)

difference_set2 = B - A
print("Difference of Set(B - A) : " , difference_set2)
