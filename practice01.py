# Please enter a positive whole number (an integer).
# I'll then show you all the numbers from 0 to N, and say whether each one is even or odd.

while True:
    try:

        n = int(input("Enter a positive integer number: "))
        if n < 0:
            print("Please enter a positive number.")
        else:
            break  # entrada valida
    except ValueError:
        print("Error: please enter valid whole numbers only")

# After the input has been validated

results = []
for i in range(n + 1):
    if i % 2 == 0:
        results.append(f"{i} é par")
    else:
        results.append(f"{i} é impar")
# Print of the last 10 numbers
print("/nUltimos resultados:")
for line in results[-10:]:
    print(line)


# I added a check during input to prevent errors,
# and limited the output to show only the last 10 numbers to avoid information overload
# and prevent issues with excessively large numbers.
