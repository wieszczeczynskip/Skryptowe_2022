produkt = "%-10s %6d %3d %6.2f"

print("Product    Amount Vat  Price")
print(produkt % ("Bread", 2, 23, 5))
print(produkt % ("Fuel", 50, 0, 499.99))
print(produkt % ("Water", 6, 23, 10))
print(produkt % ("Pen", 1, 8, 1.50))
print(produkt % ("Lolipop", 1, 23, 0.20))
