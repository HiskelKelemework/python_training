grades = [
    [87, 12, 16, 24],
    [32, 44, 22, 14, 25],
    [11, 17, 22, 14, 96]
]

# print(len(grades))
# print(grades[2][4])  # 96
# print(grades[0][0])  # 12

# there are 3 courses
# accept the number of students
# for each student, accept the grade for each of the 3 courses
# add the grades for the 3 courses to a grades list.

numOfStudents = int(input("enter the number of students: "))
numOfCourses = int(input("enter the number of courses: "))
grades = []
minGrades = []
maxGrades = []

for i in range(numOfStudents):
    ith_grades = []
    for j in range(numOfCourses):
        grade = float(input("enter " + str(j) +
                      "th grade for student " + str(i) + ": "))
        ith_grades.append(grade)

    grades.append(ith_grades)

    if i == 0:
        for l in range(numOfCourses):
            minGrades.append(ith_grades[l])
            maxGrades.append(ith_grades[l])

    for k in range(numOfCourses):
        if ith_grades[k] < minGrades[k]:
            minGrades[k] = ith_grades[k]

        if ith_grades[k] > maxGrades[k]:
            maxGrades[k] = ith_grades[k]

print(grades)
print(minGrades)
print(maxGrades)
