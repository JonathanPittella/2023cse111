from datetime import datetime

current_day = datetime.now()
today = current_day.weekday()

#Used for testing different days
today = 1

discount_rate = 0.10
sales_tax = 0.06

while True:
    number = int(input("Please, press the right number to start shopping (0 to quit):"))
    if today == 6:
        print("10 But the seventh day is the sabbath of the Lord thy God: in it thou shalt not do any work, thou, nor thy son, nor thy daughter, thy manservant, nor thy maidservant, nor thy cattle, nor thy astranger that is within thy gates: \n11 For in asix days the Lord made heaven and earth, the sea, and all that in them is, and rested the seventh day: wherefore the Lord bblessed the sabbath day, and challowed it. \n Exodus 20:10-11.")
        print("This is a joke(But is serious)") 
        break
    if number != 0:
        print("Incorrect number...")
        continue  # Continue to the next iteration if the number is not 0

    subtotal = float(input("Please enter the subtotal: "))

    if subtotal >= 50 and (today == 1 or today == 2):
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount amount: ${discount:.2f}")
        subtotal -= discount

    tax_calc = round(subtotal * sales_tax, 2)
    print(f"Sales tax amount: ${tax_calc:.2f}")

    total = subtotal + tax_calc
    print(f"Total: ${total:.2f}")

    if subtotal > 50: #and(today != 1 or today != 2):

        discount_rate = 0.10
        sales_tax = 0.06

        discount = round(subtotal * discount_rate, 2)

        subtotal -= discount

        tax_calc = round(subtotal * sales_tax, 2)

        total_one = round(subtotal + tax_calc, 2)

        total_save = total - total_one
        print("Thanks for using our service, but you are not using all your benefits...")
        print(f"If You buy those products on Tuesday or Wednesday the total yould be {total_one:.2f}")
        print(f"You would save {total_save:.2f}")

    if number == 0:
        break  # Exit the loop if 0 is entered 

