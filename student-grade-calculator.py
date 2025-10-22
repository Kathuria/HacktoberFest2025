"""
🎓 Student Grade Calculator
Author: Open for Hacktoberfest Contributions
--------------------------------------------
Takes student marks as input, calculates total, percentage, and grade.
"""

import json

def get_student_data():
    print("\n📘 Enter Student Details")
    name = input("Student Name: ")
    subjects = {}
    while True:
        subject = input("\nEnter subject name (or press Enter to finish): ")
        if not subject:
            break
        try:
            marks = float(input(f"Enter marks for {subject} (out of 100): "))
            if 0 <= marks <= 100:
                subjects[subject] = marks
            else:
                print("❌ Marks should be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter numeric value.")
    return {"name": name, "subjects": subjects}


def calculate_grade(student):
    marks = list(student["subjects"].values())
    total = sum(marks)
    percentage = total / len(marks) if marks else 0

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return {
        "name": student["name"],
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
    }


def save_result(result):
    try:
        with open("grades.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(result)
    with open("grades.json", "w") as f:
        json.dump(data, f, indent=4)
    print("\n💾 Result saved to grades.json")


def display_result(result):
    print("\n📊 Student Result Summary")
    print("-" * 35)
    print(f"Name       : {result['name']}")
    print(f"Total Marks: {result['total']}")
    print(f"Percentage : {result['percentage']}%")
    print(f"Grade      : {result['grade']}")
    print("-" * 35)


def main():
    print("🎓 Welcome to Student Grade Calculator")
    print("-" * 40)

    student = get_student_data()
    if not student["subjects"]:
        print("❌ No subjects entered. Exiting...")
        return

    result = calculate_grade(student)
    display_result(result)
    save_result(result)

    again = input("\nWould you like to add another student? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("\n✅ All done! Goodbye!")


if __name__ == "__main__":
    main()
