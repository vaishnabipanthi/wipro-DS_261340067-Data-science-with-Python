def student_average():
    students_records = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60]
    }
    
    name = input("Enter a name: ")
    if name in students_records:
        marks = students_records[name]
        average = sum(marks) / len(marks)
        print(f"Average percentage mark: {average:g}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    student_average()