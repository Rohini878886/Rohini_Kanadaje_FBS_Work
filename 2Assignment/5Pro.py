#WAP to calculate selling price of book based on a cost price and discount

c = float(input("enter the cost price of book:"))
d = float(input("enter the discount in percentahe(%):"))

selling_price = c*(1-d/100)

print(f"the selling price of book is:{selling_price}")