# task
# accept an integer from the user
# write code that computes the factorial of that number
# the factorial of a given number is the multiplication of every
# number that is less than or equal to the starting number,
# up until one.

# 6: 6 * 5 * 4 * 3 * 2 * 1

# n = int(input("enter the number: "))
# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(factorial)

# n = int(input("enter the number: "))
# m = int(input("enter the number of items u want: "))


def factorial(n):
    fact = 1
    for j in range(1, n + 1):
        fact *= j

    return fact


def combination(n, m):
    factorial_n = factorial(n)
    factorial_nm = factorial(n - m)
    factorial_m = factorial(m)

    result = factorial_n / (factorial_nm * factorial_m)
    return result


# print(combination(3, 2))
# print(combination(4, 2))
# print(combination(5, 3))

# write a function that accepts a list of numbers and
# returns the sum.

def sumList(list):
    total = 0

    for i in range(len(list)):
        total += list[i]

    return total


sumOfNumbers = sumList([2, 5, 9])
print(sumOfNumbers)

sumOfNumbers2 = sumList([77, 12, 159])
print(sumOfNumbers2)


def power(n, m):
    result = 1

    for i in range(m):
        result *= n

    return result


print(power(10, 6))  # 8
