# Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results

n = int(input("Enter the number : "))
import math
print("Square root :",math.sqrt(n))
print("Logarithm: ",math.log(n))
print("Sine: ",math.sin(n))