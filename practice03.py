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
        n = int(input("Adicione um numero inteiro positivo: "))

        if n < 0:
            print("Por favor adicione um numero positivo: ")
        else:
            break
    except ValueError:
        print("Por favor aidicone um numero valido: ")
