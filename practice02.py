# Please enter a positive whole number.
# I’ll show you the multiplication table for that number, from 1 to 10.
# If the number is greater than 100, I’ll only show the last 3 results to keep the screen clean.
# If you type something invalid (like a letter, symbol, or negative number), you’ll be asked to try again.

while True:
    try:

        n = int(input("Digite um numero inteiro positivo: "))
        if n < 0:
            print("Por favor digite um numeor inteiro positivo: ")
        else:
            break
    except ValueError:
        print("Por favor digite um numero inteiro valido: ")


for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
