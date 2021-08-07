# 1
# 2 1
# 3 2 1
# 4 3 2 1

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     print()

#    1
#   123
#  12345
# 1234567

# line i 1, 5

# 5 - i for the number of spaces
# 2 * (i - 1) + 1 for the  numbers on a line.

# for i in range(1, 5):
#     for j in range(1, 5 - i + 1):
#         print(" ", end="")

#     for k in range(1, 2 * (i - 1) + 1 + 1):
#         print(k, end="")

#     print()

# 0 1 2 3 4 5
# 1 2 3 4 5 0
# 2 3 4 5 0 1
# 3 4 5 0 1 2
# 4 5 1 0 2 3

for j in range(25):
    for i in range(j, j + 8):
        print(i % 8, end=" ")
    print()
