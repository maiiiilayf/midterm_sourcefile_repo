"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return "Excellent", "Passed"
    elif grade >= 85:
        return "Very Good", "Passed"
    elif grade >= 80:
        return "Good", "Passed"
    elif grade >= 75:
        return "Satisfactory", "Passed"
    else:
        return "Needs Improvement", "Failed"


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                
                if not line or line.startswith("#"):
                    continue

                fields = line.split(",")
                if len(fields) != 3:
                    continue

                student_id, name, grade_text = fields
                student_id = student_id.strip()
                name = name.strip()
                grade_text = grade_text.strip()

                try:
                    grade = float(grade_text)
                except ValueError:
                    continue

                if grade < 0 or grade > 100:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total_grade += student["grade"]

        _, status = classify_grade(student["grade"])
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if student["grade"] > highest_student["grade"]:
            highest_student = student

        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "count": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    print(f"\n{'Student No.':<12} {'Name':<20} {'Grade':>6} {'Classification':<18} {'Status'}")
    print("-" * 70)

    for student in students:
        classification, status = classify_grade(student["grade"])
        name = student["name"][:20]
        print(f"{student['student_id']:<12} {name:<20} {student['grade']:>6.2f} "
              f"{classification:<18} {status}")


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if statistics is None:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['count']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    keyword = keyword.strip().lower()

    for student in students:
        if keyword in student["student_id"].lower() or keyword in student["name"].lower():
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE ANALYZER - CLASS REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"{'Student No.':<12} {'Name':<20} {'Grade':>6} "
                       f"{'Classification':<18} {'Status'}\n")
            file.write("-" * 70 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                name = student["name"][:20]
                file.write(f"{student['student_id']:<12} {name:<20} "
                          f"{student['grade']:>6.2f} {classification:<18} {status}\n")

            if statistics is not None:
                file.write("\nCLASS STATISTICS\n")
                file.write(f"Number of students: {statistics['count']}\n")
                file.write(f"Class average: {statistics['average']:.2f}\n")
                file.write(f"Passed: {statistics['passed']}\n")
                file.write(f"Failed: {statistics['failed']}\n")
                file.write(f"Highest: {statistics['highest']['name']} - "
                          f"{statistics['highest']['grade']:.2f}\n")
                file.write(f"Lowest: {statistics['lowest']['name']} - "
                          f"{statistics['lowest']['grade']:.2f}\n")

        print(f"Report successfully saved to '{filename}'.")

    except OSError:
        print(f"Error: Could not write to '{filename}'.")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter a student number or name to search: ").strip()
            results = search_student(students, keyword)
            if results:
                display_students(results)
            else:
                print("No matching student found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
