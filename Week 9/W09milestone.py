import csv

def read_dictionary(filename, key_column_index):
    data = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            key = row[key_column_index]
            data[key] = row
    return data

def main():
    products_filename = 'Week 9/products.csv'
    requests_filename = 'Week 9/request.csv'

    products_data = read_dictionary(products_filename, key_column_index=0)
    requests_data = read_dictionary(requests_filename, key_column_index=0)

    print("All Products")
    print(products_data)
    print()

    print("Requested Items")
    for request in requests_data.values():
        quantity = int(request[1])
        description, price = products_data[request[0]][1:]
        total_price = quantity * float(price)
        print(f"{description}: {quantity} @ {price} - Total: {total_price:.2f}")

if __name__ == "__main__":
    main()
