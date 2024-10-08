# void function example

def main():
    print("This program converts a temperature in Fahrenheit to Celsius.")
    fahrenheit = float(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature is", celsius, "degrees Celsius.")


main()
