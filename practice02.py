# Please enter a positive whole number.
# I’ll show you the multiplication table for that number, from 1 to 10.
# If the number is greater than 100, I’ll only show the last 3 results to keep the screen clean.
# If you type something invalid (like a letter, symbol, or negative number), you’ll be asked to try again.

while True:
    try:

        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer: ")
        else:
            break
    except ValueError:
        print("Please enter a valid integer: ")


result_list = []

for i in range(1, 11):
    result_list.append(f"{n} x {i} = {n * i}")

if n > 100:
    print("Result is too large. Showing only the last 3 items.")
    for line in result_list[-3:]:
        print(line)
else:
    for line in result_list:
        print(line)
