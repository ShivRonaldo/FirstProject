# Dictionary storing student details
students = {
    101: {"name": "Arnav", "age": 12, "class": "7th", "marks": 85},
    102: {"name": "Riya", "age": 13, "class": "8th", "marks": 90},
    103: {"name": "Rahul", "age": 12, "class": "7th", "marks": 78}
}

# Take input from user
code = int(input("Enter student code: "))

# Check and display details
if code in students:
    print("Student Details:")
    print("Name:", students[code]["name"])
    print("Age:", students[code]["age"])
    print("Class:", students[code]["class"])
    print("Marks:", students[code]["marks"])
else:
    print("Student not found!")
