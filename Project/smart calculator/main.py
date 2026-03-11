import arithmetic
import bmi
import temperature
import lenght


def main():
    while True:
        print("\n===== SMART CALCULATOR =====")
        print("1. Arithmetic Operations")
        print("2. BMI Calculator")
        print("3. Temperature Converter")
        print("4. Length Converter")
        print("5. Exit")

        choice = input("Select option: ")

    
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                print("1. Add")
                print("2. Subtract")
                print("3. Multiply")
                print("4. Divide")

                op = input("Choose operation: ")

                if op == "1":
                    print("Result:", arithmetic.add(a, b))
                elif op == "2":
                    print("Result:", arithmetic.subtract(a, b))
                elif op == "3":
                    print("Result:", arithmetic.multiply(a, b))
                elif op == "4":
                    print("Result:", arithmetic.divide(a, b))
                else:
                    print("Invalid operation!")

            except ValueError:
                print("Invalid input! Please enter numbers.")

        
        elif choice == "2":
            try:
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (feet): "))
                inches = float(input("Enter inches (inches): "))

                bmi_value = bmi.calculate_bmi(weight, height, inches)
                category = bmi.bmi_category(bmi_value)

                print("BMI:", round(bmi_value, 2))
                print("Category:", category)

            except ValueError:
                print("Invalid input!")

        
        elif choice == "3":
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")

            temp_choice = input("Choose option: ")

            try:
                if temp_choice == "1":
                    c = float(input("Enter Celsius: "))
                    print("Fahrenheit:", temperature.c_to_f(c))
                elif temp_choice == "2":
                    f = float(input("Enter Fahrenheit: "))
                    print("Celsius:", temperature.f_to_c(f))
                else:
                    print("Invalid option!")

            except ValueError:
                print("Invalid input!")

        
        elif choice == "4":
            print("1. Meters to KM")
            print("2. KM to Meters")
            print("3. Meters to Feet")
            print("4. Feet to Meters")

            lenght_choice = input("Choose option: ")

            try:
                if lenght_choice == "1":
                    m = float(input("Enter meters: "))
                    print("KM:", lenght.meters_to_km(m))
                elif lenght_choice == "2":
                    km = float(input("Enter KM: "))
                    print("Meters:", lenght.km_to_meters(km))
                elif lenght_choice == "3":
                    m = float(input("Enter meters: "))
                    print("Feet:", lenght.meters_to_feet(m))
                elif lenght_choice == "4":
                    f = float(input("Enter feet: "))
                    print("Meters:", lenght.feet_to_meters(f))
                else:
                    print("Invalid option!")

            except ValueError:
                print("Invalid input!")

        
        elif choice == "5":
            print("Program Ended Successfully ")
            break

        else:
            print("Invalid menu option!")

main()