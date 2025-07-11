#arrays in python

# 1. Creating an array

import array


# Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print(f"Integer Array: {int_array}")    

print(int_array[0])  # Accessing the first element


float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(f"Float Array: {float_array}")

# Create an array of characters
char_array = array.array('u', 'Hello')  
print(f"Character Array: {char_array}")


#empty array of size 10
empty_array = array.array('i', [0]*10)  # Empty array of integers
print(f"Empty Integer Array: {empty_array}")

print(len(empty_array))  # Length of the array

empty_array.append(6)  # Append an element
print(f"Array after appending 6: {empty_array}")    