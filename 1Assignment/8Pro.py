# write a program to convert days into years, weeks and days

days = int(input("enter a days:"))

y = days // 365
day = days % 365
w = day // 7
d = days % 7

print(f"year:{y},weeks:{w},days:{d}")
