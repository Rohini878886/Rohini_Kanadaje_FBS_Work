 # write a program to enter P,T,R and calculate compount interest


P = float(input("enter a principle amount (P):"))
T = float(input("enter a Time (T):"))
R = float(input("enter a price (R) (R in %):"))
 
# A= Final amount
ci = P * ((1 + R / 100) ** T)-P
print(f"compount interest is:{ci}") 
 