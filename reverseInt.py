#!/usr/bin/env python3

def reverse(array):
    # Reverse the array using slicing
    reversed_array = array[::-1]
    return reversed_array

# Input from the user
user_input = input("Please enter integers separated by spaces: ")
# Convert the input string to a list of integers
int_array = list(map(int, user_input.split()))
# Call the reverse function
reversed_result = reverse(int_array)
print("Reversed array:", reversed_result)

