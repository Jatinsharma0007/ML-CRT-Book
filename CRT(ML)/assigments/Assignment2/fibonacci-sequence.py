def generate_fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

def print_fibonacci_sequence():
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

        if num_terms < 1:
            print("Please enter a positive integer.")
            return

        fibonacci_series = generate_fibonacci(num_terms)

        print(f"\nFibonacci Sequence with {num_terms} terms:")
        print(fibonacci_series)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print_fibonacci_sequence()