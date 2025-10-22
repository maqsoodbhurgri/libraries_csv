import csv

header = ["id", "name", "price", "quantity"]
products = [
    [1, "Laptop", 1200, 3],
    [2, "Mouse", 400, 10],
    [3, "Keyboard", 600, 5],
    [4, "Monitor", 15000, 2]
]

with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(products)

total_value = 0
print("\nProducts with price > 500:")

with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total_value += price * quantity
        if price > 500:
            print(row)

print(f"\nTotal value of all products: {total_value}")

new_product = [5, "Headphones", 800, 4]
with open("products.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_product)

print("\nNew product added successfully!")
