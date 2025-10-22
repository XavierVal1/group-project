"""
File 1 (problem1.py): Write a function to reverse a string.

Example:
Input: "Hello"
Output: "olleH"

Understand
Problem: Right a function that takes in a string parameter, iterates through it, and print it out in the reversed order
Input: String Parameter
Output: Reversed String
Edge Cases - Empty String
Clues: Function, For loop, return

Write pseudocode.
1. define a function as take in 1 string parameter
2. set the new reversed string variable equal to as empty string
3. interate through the string parameter by tracking each character
4. For each iteration, add the character at the index to the front of reversed string
5. When for loop terminates, return reversed string
6. Test function by making a call to the function with "hello" and edge case
7. Print the output.

"""

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

test1 = reverse_string("hello")
test2 = reversestring("")
print(test1)
print(test2)
