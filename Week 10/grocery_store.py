import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

TAX_RATE = 0.06  # 6% sales tax rate

def load_products(products_file_path):
    products = {}
    with open(products_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item_name = row['Item Name']
            price = float(row['Price'])
            products[item_name] = price
    return products

def display_products(products):
    print("Welcomde to the Modern Grocery, where you can literaly shop for yourself!")
    print()
    print("Available Products:")
    print("-------------------")
    for item, price in products.items():
        print(f"{item}: ${price:.2f}")
    print("-------------------")

def get_customer_shopping_list(products):
    customer_list = {}
    while True:
        item_name = input("Enter an item name (or 'done' to finish): ").capitalize()
        if item_name.lower() == 'done':
            break
        elif item_name in products:
            try:
                quantity = int(input(f"How many {item_name}s do you want? "))
                customer_list[item_name] = quantity
            except KeyError:
                print("Error: Please enter a valid number.")
            
        else:
            print("Error: Please choose from the available products.")

    return customer_list

def process_order(customer_name, items, products):
    print(f"\nReceipt for {customer_name}:")
    print("--------------------------")
    
    subtotal = 0
    total_items = 0  # Variable to keep track of total quantity

    for item_name, quantity in items.items():
        if item_name in products:
            price = products[item_name]
            item_total = quantity * price
            subtotal += item_total
            total_items += quantity  # Update the total quantity
            print(f"{item_name} x{quantity}: ${item_total:.2f}")
            print(f"Ordered items: {quantity}")
        else:
            print(f"Unknown item: {item_name}")

    sales_tax = subtotal * TAX_RATE
    total = subtotal + sales_tax

    print("--------------------------")
    print(f"Subtotal: ${subtotal:.2f}") # Print the total for just the ordened items
    print(f"Sales Tax ({TAX_RATE*100}%): ${sales_tax:.2f}") #Print the tax rate(For that code is 6%)
    print(f"Total: ${total:.2f}") # Print the total price + the tax rate
    print(f"Total items: {total_items}")  # Print the total quantity
    print()
    print("Thanks for shopping with us!")
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")
    print("\n")

    return subtotal, sales_tax, total

def update_requests_csv(requests_csv_path, customer_name, items, subtotal, sales_tax, total, current_date_and_time):
    with open(requests_csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([customer_name, items, subtotal, sales_tax, total, current_date_and_time])

def main():
    try:    
        products_csv_path = 'Week 10/products.csv'
        requests_csv_path = 'Week 10/request.csv'

        products_data = load_products(products_csv_path)
        display_products(products_data)

        customer_name = input("Enter the customer's name: ")
        customer_list = get_customer_shopping_list(products_data)

        subtotal, sales_tax, total = process_order(customer_name, customer_list, products_data)

        current_date_and_time = datetime.now()
        update_requests_csv(requests_csv_path, customer_name, customer_list, subtotal, sales_tax, total, current_date_and_time)

    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {products_csv_path} doesn't exist.")
        print("The files 'grocery_store.py', 'products.csv' and 'request.csv' must be stored in the same folder!")
    else:
        print("\nOrder processed successfully!")

if __name__ == "__main__":
    main()