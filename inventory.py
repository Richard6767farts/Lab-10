#Reflection
#Q1) I expected lists to work like a fixed table in Excel, but Python lists can grow, shrink, 
# and reorder with simple methods like .append(), .remove(), and .sort(). What surprised 
# me most was that slicing can grab a whole section of a list in one line,
# like [::2] pulling every other item, instead of selecting cells one by one.

#Q2) In my hospitality class we looked at how restaurants track food and supply 
# inventory, which ties into my goal of becoming a restaurant manager. In Excel, 
# checking which items are running low means scrolling, sorting, and filtering by 
# hand every time. With a Python list and a loop, I could flag low-stock items, count 
# them, and rerun the same check each week in seconds.



#Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2
print("---Exercise 2: Index Practice---")
print(inventory[0]) 
print(inventory[-1]) 

middle = len(inventory) // 2
print(inventory[middle]) 

#Exercise 3
print("---Exercise 3: Slicing Practice---")
print(inventory[:3]) 
print(inventory[-2:]) 
print(inventory[::2]) 

print("---Exercise 4: List Methods---")
inventory.append("envelope") 
print(inventory)
inventory.remove("tape") 
print(inventory)
inventory.sort() 
print(inventory)

print("---Exercise 5: Tuple comparison---")
coords = (40.7128, -74.0060) 
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

print("---Exercise 6: Average of a list of sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"The total sales is: {total}")
print(f"The number of sales is: {count}")
print(f"The average sales is: {average}")
print(f"The best sale is: {max(sales)}")
print(f"The worst sale is: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"The best sale is: {best}")
print(f"The worst sale is: {worst}")

print("---Exercise 7: Accumulator pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

print("---Exercise 8: Filter above threshold---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
