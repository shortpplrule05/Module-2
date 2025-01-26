print("Enter student last name:")
student_last=input()
while student_last == "ZZZ":
    break
else: 
    print("Enter student first name:")
    student_first = input()
    print("Enter student GPA:")
    gpa = float(input())
    if gpa >= 3.5:
        print(student_first, student_last, "made the Dean's List.")
    elif gpa >= 3.25:
        print(student_first, student_last, "made the Honor Roll.")
    else:
        print(student_first, student_last, "did not make either list.")