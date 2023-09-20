from datetime import datetime

import math

current_day = datetime.now()

today = current_day.date()

width_mm = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter_inches = float(input("Enter the diameter of the wheel in inches: "))

volume_litters = math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inches) / 10000000000

with open("volumes.txt", "at") as volumes_file:

    print(f"{today}, {int(width_mm)}, {int(aspect_ratio)}, {int(diameter_inches)}, {volume_litters:.2f}", file=volumes_file)