def print_divisible_by_three(numbers):
    for num in numbers:
        if num % 3 != 0:
            continue
        print(num)


numbers = [1, 3, 5, 6, 9, 10, 12, 15, 18]
print("Numbers divisible by 3:")
print_divisible_by_three(numbers)