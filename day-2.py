def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"


def main():
    while True:
        try:
            marks = float(input("Enter the marks obtained by the student: "))
            if marks < 0 or marks > 100:
                print("Invalid input! Marks should be between 0 and 100.")
            else:
                grade = calculate_grade(marks)
                print("Grade: ", grade)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        choice = input(
            "Do you want to calculate the grade for another student? (y/n): ")
        if choice.lower() != "y":
            break


if __name__ == "__main__":
    main()
