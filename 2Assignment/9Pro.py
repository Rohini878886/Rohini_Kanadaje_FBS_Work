# WAP to swap two number without using third variable

no1 = int(input("enter the first number:"))
no2 = int(input("enter the second number:"))

# before swaping
print(f"Before swaping no1:{no1},no2:{no2}")
no1,no2 = no2,no1      

# after swaping
print(f"after swaping no1:{no1},no2:{no2}")