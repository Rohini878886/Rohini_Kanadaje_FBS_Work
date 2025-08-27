# convert given distance in feet  and inches into meter and centimeter
f = float(input("enter the feet:"))
i = float(input("enter the inches:"))

feet_into_meter = f*0.3048
feet_into_centimeter = f*30.48
inc_into_meter = i*0.0254
inc_into_centimeter = i*2.54

print(f"distance in feet into meter:{feet_into_meter}, distance in feet into centimeter:{feet_into_centimeter}")
print(f"distance in inches into meter:{inc_into_meter}, distance in inches into centimeter:{inc_into_centimeter}")
