#  Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.
n = input("Enter the Student's Name: ")
Student_Dict= { 'Alice':85 , 'Smarajit':100, 'Rahul':90,'Ramesh':20,'Raju':15}
for keys , values in Student_Dict.items():
    if (keys == n):
     print(f"{n}'s Marks: ",values)
     break
else:
    print("Student Not found")