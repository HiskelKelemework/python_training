# stud = []
# stud.append(1)
# stud.append(13)
# stud.append(21)

# print(stud)
# # access/read
# # print(stud[3])
# # change/write
# stud[1] = 44
# print(stud[1])
# # adding elements
# stud.append(123)
# stud.insert(2, 90)
# print(stud)
# # delte
# stud.remove(123)
# stud.pop(0)

# print(stud)

# stud.extend([1, 2, 3])
# print(stud)

# accept the number of students
# accept each student's grade and put it in a list.
# identify the minimum grade
# identify the maximum grade
# calculate the average grade

numOfStudents = int(input("enter the number of students: "))
grades = []

totalGrade = 0
minGrade = 0
maxGrade = 0

for i in range(numOfStudents):
    grade = float(input("enter the student's grade: "))
    grades.append(grade)

    totalGrade += grade

    if i == 0:
        minGrade = grade
        maxGrade = grade

    if grade < minGrade:
        minGrade = grade
    if grade > maxGrade:
        maxGrade = grade

# print(grades)

# minGrade = grades[0]
# maxGrade = grades[0]
# totalGrade = 0

# for i in range(numOfStudents):
#     if grades[i] < minGrade:
#         minGrade = grades[i]
#     if grades[i] > maxGrade:
#         maxGrade = grades[i]

#     totalGrade += grades[i]

print("mininum value", minGrade)
print("maximum value: ", maxGrade)
print("total grade is: ", totalGrade)
print("the average grade is ", totalGrade / numOfStudents)
