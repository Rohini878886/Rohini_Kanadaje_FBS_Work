# write a program to enter P,T,R and calculate simple interest

P = int(input("enter price p:"))
T = int(input("enter time T:"))
R = int(input("enter rate R:"))

SI = P * T * R / 100

print(f"simple interest is:{SI}")