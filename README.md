# bootcampPython
My learnings from Python



Projects: 

# Meat Doneness Checker 🥩

A simple Python program that asks the user for the internal temperature of a piece of meat (in Celsius) and returns the corresponding doneness level (e.g., rare, medium, well done).

This is a beginner-level project focused on input validation, conditional logic, and clean code practices in Python.

## 🔧 How It Works

1. The user is prompted to enter the temperature of the meat.
2. The input is validated to ensure it's a whole number (integer).
3. Based on the temperature, the program prints the doneness level:

| Temperature (°C) | Doneness Level  |
|------------------|------------------|
| < 48             | Undercooked      |
| 48–53            | Rare             |
| 54–59            | Medium Rare      |
| 60–65            | Medium           |
| 66–71            | Medium Well      |
| > 71             | Well Done        |

## 🧪 Example

```bash
What is the meat temperature in Celsius? 60
The meat is medium.

