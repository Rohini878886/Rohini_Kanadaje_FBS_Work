l = int(input("enetr the length :"))
b = int(input("enetr the breadth :"))
r = int(input("enter the radius:"))
pi = 3.14
area_of_rectangle = l * b
area_of_semicircle = 0.5 * pi * r**2
total_area = area_of_rectangle + area_of_semicircle  
peri = (2 * l) + b + (pi * r )

print(f"area of figure is:{total_area}")
print(f"perimeter of figure is:{peri}")
