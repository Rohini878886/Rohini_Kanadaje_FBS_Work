# convert the time entered in hh, min, and second into second

h = float(input(" Enter the hours:"))
min = int(input("Enter the minutes:"))
sec = int(input("Enter the seconds:"))

hou_to_sec = h*3600
min_to_sec = min*60
tot_sec = hou_to_sec + min_to_sec

print (f" time hours to second is:{hou_to_sec}")
print (f" time minute to second is:{min_to_sec}")
print (f"total second is:{tot_sec}")

