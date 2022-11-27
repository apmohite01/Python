marks=[90,83,57,"maths"]
print(marks)
print(marks[2])

print(marks[0:3])

print(marks[0:-1])

print(marks[0:-3])
print(marks[0:7])
marks.append(99)
print(marks)
marks.insert(0,80)
print(marks)

print(99 in marks)
print(len(marks))

i=0
while(i<len(marks)):
    print(marks[i])
    i=i+1
marks.clear()
print(marks)