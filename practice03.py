# Please enter a positive integer.
# I’ll calculate the factorial of that number using a separate function called calculate_factorial(n).
# If the number is greater than 50, I’ll let you know it’s a large value and show only the last 5 steps of the calculation.

def calculate_factorial(n):
    result = 1
    steps = []

    for i in range(n, 0, -1):
        result *= i
        steps.append(i)

    return result, steps


while True:

    try:
        n = int(input("Enter a positive integer: "))

        if n < 0:
            print("Please enter a positive integer: ")
        else:
            break
    except ValueError:
        print("Please enter a valid integer: ")

factorial_result, steps = calculate_factorial(n)

if n > 50:
    print("Value too large. Showing last 5 steps only:")
    print("... x " + " x ".join(str(i)
          for i in steps[-5:]) + f" = {factorial_result:.6e}")
else:
    print(f"{n}! = " + " x ".join(str(i)
          for i in steps) + f" = {factorial_result}")
