def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))

        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

    except ValueError:
        print("Please enter a valid year (a whole number).")


if __name__ == "__main__":
    main()
