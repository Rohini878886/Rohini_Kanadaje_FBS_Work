# write a program to calculate the percentage of student based on marks of any 5 subject

s1 = int(input('enter a student subject marks: s1'))
s2 = int(input('enter a student subject marks: s2'))
s3 = int(input('enter a student subject marks: s3'))
s4 = int(input('enter a student subject marks: s4'))
s5 = int(input('enter a student subject marks: s5'))

tot_marks = s1 + s2 + s3 + s4 + s5

perc = (tot_marks / 500) * 100

print (f'total percentage of student is:{perc} %')