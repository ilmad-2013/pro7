
print("================================")
print("      STUDENTS MARKS ANALYZER")
print("================================")

students = []
marks = []

number = int(input("Enter number of students: "))

if number <= 0:
    print("Please enter a valid number of students.")

else:
    for i in range(number):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")
        mark = float(input("Enter student mark: "))

        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a mark from 0 to 100.")
            continue

        students.append(name)
        marks.append(mark)

    print("\n========== CLASS REPORT ==========")

    passed = 0
    failed = 0

    for i in range(len(students)):
        print("\nName:", students[i])
        print("Mark:", marks[i])

        if marks[i] >= 50:
            print("Status: Passed")
            passed += 1
        else:
            print("Status: Failed")
            failed += 1

    if len(marks) > 0:
        average = sum(marks) / len(marks)

        print("\n========== CLASS ANALYSIS ==========")
        print("Highest mark:", max(marks))
        print("Lowest mark:", min(marks))
        print("Class average:", round(average, 2))
        print("Students passed:", passed)
        print("Students failed:", failed)

        marks.sort()
        print("Sorted marks:", marks)

    else:
        print("No valid student records were entered.")
