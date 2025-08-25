# Write a program to input two angles from users and find third angle of the traingle

angle1 = int(input("enter the first angle of traingle:"))
angle2 = int(input("enter the second angle of traingle"))

angle3 = 180 - (angle1 + angle2)

print(f" the third angle of traingle is: {angle3}" )