# Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

n = input("Enter the text to write to the file: ")
file = open("C:/Users/KIIT0001/Desktop/python/Tutedude Assignments/Assignment 4/output.txt","w")
writing_file = file.write(n)
print(f"Data successfully written to {file.name}")
file.close()

n = input("Enter additional text to append : ")
file = open("C:/Users/KIIT0001/Desktop/python/Tutedude Assignments/Assignment 4/output.txt","a")
appending_file = file.write(n)
print("Data successfully appended.")
file.close()

print(f"Final content of {file.name} ")
file = open("C:/Users/KIIT0001/Desktop/python/Tutedude Assignments/Assignment 4/output.txt","r")
reading_file = file.read()
print(reading_file)
file.close()