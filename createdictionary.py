student = { "Roll_No": 100 , "Name":"Rahul" , "Marks":80 }
print("Dictionary: " , student)
print("Roll No:" , student["Roll_No"])
print("Marks: " , student["Marks"])
 
student["Marks"] = 90
student["Grade"] = "A"
print("Updated Dictionary: " , student)
print()

removed_value = student.pop("Grade")
print("Removed Value: " , removed_value)
print("After removing value: " , student)

student.popitem()
print("After popitem(): " , student)
print()

dict1 = {"a":2,"b":3}
dict2 = {"c":4,"d":5}
merged_dictionary = dict1 | dict2
print("Merged Dictionary: " , merged_dictionary)
