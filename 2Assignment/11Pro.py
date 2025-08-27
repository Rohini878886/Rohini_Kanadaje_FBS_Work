# WAP to accept an integer amount from user and tell  minimum number of notes needed for representing that amount
amount = int(input("Enter the amount:"))

n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print(" minimum no of notes:")
print("2000 x",n2000)
print("500 x",n500)
print("200 x",n200)
print("100 x",n100)
print("50 x",n50)
print("20 x",n20)
print("10 x",n10)