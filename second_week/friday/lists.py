stud = []
stud.append(1)
stud.append(13)
stud.append(21)

print(stud)
# access/read
# print(stud[3])
# change/write
stud[1] = 44
print(stud[1])
# adding elements
stud.append(123)
stud.insert(2, 90)
print(stud)
# delte
stud.remove(123)
stud.pop(0)

print(stud)

stud.extend([1, 2, 3])
print(stud)

# accept the number of students
# accept each student's grade and put it in a list.
