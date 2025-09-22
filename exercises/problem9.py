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

# Step 1: Increase Price of Furniture by 10%
df.loc[df["Category"] == "Furniture", "Price"] *= 1.10

# Step 2: Recalculate Total
df["Total"] = df["Quantity"] * df["Price"]

# Step 3: Show only Furniture rows
print(df[df["Category"] == "Furniture"])