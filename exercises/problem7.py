import pandas as pd

# Step 1: Create DataFrame
data = {
    "OrderID": range(1001, 1021),
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", 
        "Headphones", "Mouse", "Chair", "Desk", "Laptop",
        "Printer", "Keyboard", "Monitor", "Mouse", "Laptop",
        "Headphones", "Desk", "Monitor", "Printer", "Chair"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories", "Furniture", "Furniture", "Electronics",
        "Electronics", "Accessories", "Electronics", "Accessories", "Electronics",
        "Accessories", "Furniture", "Electronics", "Electronics", "Furniture"
    ],
    "Quantity": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],
    "Price": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],
    "Customer": [
        "Alice", "Bob", "Charlie", "Diana", "Ethan",
        "Fiona", "George", "Hannah", "Ian", "Jane",
        "Kyle", "Laura", "Mike", "Nina", "Oscar",
        "Paul", "Queen", "Robert", "Sarah", "Tom"
    ],
    "Region": [
        "North", "South", "East", "West", "North",
        "South", "East", "West", "North", "South",
        "East", "West", "North", "South", "East",
        "West", "North", "South", "East", "West"
    ]
}
df = pd.DataFrame(data)

# Step 1: Electronics with Quantity >= 3
result1 = df[(df["Category"] == "Electronics") & (df["Quantity"] >= 3)]
print(result1)

# Step 2: Products with Price > 500
result2 = df[df["Price"] > 500]
print(result2)

# Step 3: Count orders from North region
count_north = df[df["Region"] == "North"].shape[0]
print("North orders:", count_north)
