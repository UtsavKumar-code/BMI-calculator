 
 
def get_positive_float(prompt):
    """Prompt repeatedly until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
 
 
def calculate_bmi(weight_kg, height_m):
    """Calculate BMI given weight in kg and height in meters."""
    return weight_kg / (height_m ** 2)
 
 
def classify_bmi(bmi):
    """Return the BMI category based on standard WHO ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
 
 
def main():
    print("=" * 40)
    print("        BMI (Body Mass Index) Calculator")
    print("=" * 40)
 
    weight = get_positive_float("Enter your weight in kilograms (kg): ")
    height = get_positive_float("Enter your height in meters (m): ")
 
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
 
    print("\n--- Result ---")
    print(f"Weight: {weight:.2f} kg")
    print(f"Height: {height:.2f} m")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
 
    print("\nBMI Categories Reference:")
    print("  Underweight    : BMI < 18.5")
    print("  Normal weight  : 18.5 <= BMI < 25")
    print("  Overweight     : 25 <= BMI < 30")
    print("  Obese          : BMI >= 30")
 
 
if __name__ == "__main__":
    while True:
        main()
        again = input("\nWould you like to calculate another BMI? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Stay healthy.")
            break
        print()
 