# Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
try:
    file = open('C:/Users/KIIT0001/Desktop/python/Tutedude Assignments/Assignment 4/sample.txt','r')
    reading_file = file.read()
    print(reading_file)
    file.close()
    print("The file exists")
except FileNotFoundError:
    print("The file does not exist")
