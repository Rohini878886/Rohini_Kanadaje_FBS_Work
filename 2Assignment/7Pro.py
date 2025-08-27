# find the sum of three digit number

no = int(input("Enter the three digit no:"))
no1 = no // 10
d1 = no % 10
no2 = no1 // 10
d2 = no1 % 10
no3 = no2 // 10
d3 = no2 % 10

sum = d1+d2+d3

print(f"sum of three digit no is:{sum}")