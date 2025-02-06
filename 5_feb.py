a = int(input("Enter the number of copies sold: "))
b = float(input("Enter the price per copy (Rs.): "))
c = float(input("Enter the cost per copy (Rs.): "))

revenue = a * b
cost = (a * c) + 100
profit = revenue - cost


print(f"The profit obtained on Saturday is: Rs. {profit:.2f}")
