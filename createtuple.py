tuple1 = (1,2,3,4,5,6)
print("Tuple 1: " , tuple1)
print("First Element: " , tuple1[0])
print("Last Element: " , tuple1[-1])

nested_tuple = (1,2,3,(4,5,6),7)
print("Nested Tuple: " , nested_tuple)
print("Nested Tuple Elements: " , nested_tuple[3])

tuple2 = (1,2)
repeated_tuple = tuple2*3
print("Repeated Tuple 2 (1,2): " , repeated_tuple)

tuple3 = (10,20,30)
tuple4 = (40,50,60)
concatenated_tuple = tuple3 + tuple4
print("Concatenated Tuple: " , concatenated_tuple)
