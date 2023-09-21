from datetime import datetime
import math

def calculate_tire_volume(start):
    while True:
        if start == "0": 
            width_mm = float(input("Enter the width of the tire in mm: "))
            aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
            diameter_inches = float(input("Enter the diameter of the wheel in inches: "))

            volume_liters = math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inches) / 10000000000

            name = ""  
            phone = "" 

            buy_tires = input("Do you want us to search for a tire with those dimensions? Press y/n: ")
            if buy_tires == "y":
                print("Please set your contact information:")
                name = input("Full name: ")
                phone = input("Phone number: ")

                with open("volumes.txt", "a") as volumes_file:
                    print(f"{today}, {int(width_mm)}, {int(aspect_ratio)}, {int(diameter_inches)}, {volume_liters:.2f}\n{name}, - {phone}.", file=volumes_file)
                print()
                print("We will search for your tire and contact you!")
                break
            elif buy_tires == "n":
                with open("volumes.txt", "a") as volumes_file:
                    print(f"{today}, {int(width_mm)}, {int(aspect_ratio)}, {int(diameter_inches)}, {volume_liters:.2f}\n{name}, - {phone}.", file=volumes_file)
                print("Thanks for contacting! If you need our service, we are always available!")
                break
            else:
                while True:
                    again = input("Do you want to play it again? y/n: ")
                    if again == "y":
                        break
                    elif again == "n":
                        print("See you!")
                        return
                    else:
                        print("Incorrect answer. y/n:")

current_day = datetime.now()
today = current_day.date()

while True:
    start = input("Please Enter number '0' to start or 'exit' to quit: ")
    if start == "0":
        calculate_tire_volume(start)
    elif start == "exit":
        print("Goodbye!")
        break
    else:
        print("Incorrect answer. Please enter '0' to start or 'exit' to quit.")