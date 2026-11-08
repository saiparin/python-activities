import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius: "))
print(f"Circumference: {calculate_circumference(r):.2f}")