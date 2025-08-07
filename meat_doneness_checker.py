# Meat thermometer that tells you exactly how well it's cooked.

def main():
    # Step 1: Ask the user for the temperature

    while True:
        user_input = input("What is the meat temperature in Celsius? ")

        try:
            # Try to convert the input to an integer
            temperature = int(user_input)
            break
        except ValueError:
            # If the input is not a valid integer, show an error and ask again
            print("Please enter the temperature as a whole number in Celsius.")

    # Step 2: Determine the meat doneness
    if temperature < 48:
        print("The meat is undercooked")

    elif 48 <= temperature <= 53:
        print("The meeat is rare.")

    elif 54 <= temperature <= 59:
        print("The meat is medium rare.")

    elif 60 <= temperature <= 65:
        print("The meat is medium.")

    elif 66 <= temperature <= 71:
        print("The meat is medium well")

    else:
        print("The meat is well done ")


# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
