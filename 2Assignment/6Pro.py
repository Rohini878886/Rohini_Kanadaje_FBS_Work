# WAP to calculate total salary of employee based on basic,da=10% of basic, ta = 12% of basic, hra=15% of basic

s = float(input("Enter the basic salary of employee:"))

da = s*0.10
ta = s*0.12
hra = s*0.15
total_salary = s+da+ta+hra

print(f"total salary of employee:{total_salary}")


