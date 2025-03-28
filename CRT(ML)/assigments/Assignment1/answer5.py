def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def main():
    try:
        mark = float(input("Enter your mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return

        grade = calculate_grade(mark)
        print(f"Your grade is: {grade}")

    except ValueError:
        print("Error: Please enter a valid numeric mark.")


if __name__ == "__main__":
    main()
