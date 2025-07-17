### This script demonstrates various data types in Python.

# Data Types in Python
a = 1  #Integer
b = 2.3  #Float
c = "Hello" #string
d = True #Boolean
e = None #NoneType

typelist = [a, b, c, d, e]  #List

for t in typelist:
    print(f"{t} : {type(t)}")

# Tuple, list and Range 
tuple = (a, b, c, d, e)  #Tuple   
print(f"{tuple} : {type(tuple)}")  # Print the tuple and its type

my_list = [a, b, c, d, e]  #List
print(f"{my_list} : {type(my_list)}")  # Print the list and its type

range_list = list(range(5))  #Range
print(f"{range_list} : {type(range_list)}")  # Print the range list
 

#frozenset, set and dictionary  

frozenset_example = frozenset([1, 2, 3, 4])  # Frozenset
print(f"{frozenset_example} : {type(frozenset_example)}")

dict_example = {"name": "Alice", "age": 30}  # Dictionary

dict_example["city"] = "New York"  # Adding a new key-value pair
print(f"{dict_example} : {type(dict_example)}")  # Print the dictionary and