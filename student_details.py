# Dictionary storing student details
students = {
    101: {"name": "Arnav", "age": 12, "class": "7th", "marks": 85},
    102: {"name": "Riya", "age": 13, "class": "8th", "marks": 90},
    103: {"name": "Rahul", "age": 12, "class": "7th", "marks": 78},
    104: {"name": "Priya", "age": 13, "class": "8th", "marks": 92},
    105: {"name": "Vikas", "age": 12, "class": "7th", "marks": 88},
    106: {"name": "Neha", "age": 13, "class": "8th", "marks": 95},
    107: {"name": "Aditya", "age": 12, "class": "7th", "marks": 80},
    108: {"name": "Zara", "age": 13, "class": "8th", "marks": 87},
    109: {"name": "Sanjay", "age": 12, "class": "7th", "marks": 82},
    110: {"name": "Divya", "age": 13, "class": "8th", "marks": 89}
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
