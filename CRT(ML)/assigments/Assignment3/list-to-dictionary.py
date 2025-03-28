merge_lists = lambda keys, values: dict(zip(keys, values))


def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    name_age_dict = merge_lists(names, ages)

    print("Names and Ages Dictionary:")
    print(name_age_dict)

    try:
        short_names = ["David"]
        short_ages = [40, 45, 50]

        partial_dict = merge_lists(short_names, short_ages)
        print("\nPartial Dictionary (truncated to shorter list):")
        print(partial_dict)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
