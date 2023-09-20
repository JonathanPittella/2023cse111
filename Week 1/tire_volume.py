import math

width_mm = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inches = float(input("Enter the diameter of the wheel in inches: "))

volume_liters = math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inches) / 10000000000

print(f"The approximate volume is {volume_liters:.2f} liters")
