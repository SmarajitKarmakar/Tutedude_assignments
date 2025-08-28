"""Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""
A = int(input("Enter the number : "))
if(A%2 == 0):
    print(A,"is an even number ")
else:
    print(A,"is an odd number")