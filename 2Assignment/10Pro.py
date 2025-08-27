# WAP to reverce three digit no
num = int(input("Enter the three digit no:"))

hundread = num // 100
tens = (num // 10) % 10
units = num % 10
reversed_num = (units*100)+(tens*10)+hundread

print("reverce three digit no",reversed_num)