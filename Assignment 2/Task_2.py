""" Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""

s = 0
for i in range(1,51):
    s = s + i
print("The sum of numbers from 1 to 50 is : ",s)