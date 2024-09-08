#!/usr/bin/python3

# List Comprehension 
# Reference: https://www.geeksforgeeks.org/python-list-comprehension/


# Syntax: newList = [ expression(element) for element in oldList if condition ] 
# Parameter:
#   expression: Represents the operation you want to execute on every item within the iterable.
#   element: The term “variable” refers to each value taken from the iterable.
#   iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
#   condition: (Optional) A filter helps decide whether or not an element should be added to the new list.

# List comprehension with expression (multiplication)
numbers = [1, 2, 3, 4, 5, 6, 7, 8,]
doubled = [x * 2 for x in numbers]
print(doubled)


# In this example, we are assigning 1, 2, and 3 to the list and 
#   we are printing the list using List Comprehension.
# Using list comprehension to iterate through loop 
List = [character for character in [1,2,3]]
print(List)


# In this example, we are printing the even numbers from 0 to 10 using List Comprehension.
even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)


