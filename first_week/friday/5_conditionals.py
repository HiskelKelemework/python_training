age = 20

# >= 20, allowed
# rest, not

if age == 20:
    print("you can enter")
elif age == 18:
    print("you can enter through the backdoor")
else:
    print("you cannot enter")

# exercise
# accept a number from the console
# if the number is even display "even"
# if the number is evenly divisible by 5 display "multiple of five"
# if the number is not even display "odd"

# or truth table
# -------------|
#    |T  |  F |
# --------|-----
# T  | T |  T |
# F  | T |  F |
# -------------|


# accept the user's age
# accept the user's nationality
# if the person is ethiopian and the user's age is >= 18, print "you can vote"
# if the person is not ethipian and the user's age is >= 18 print "apply for citizenship"
# if the person is not ethiopian and the user's age is < 18 print("no service")

age = eval(input("enter your age: "))
nationality = input("nationality: ")

is_old_enough = age >= 18
is_ethiopian = nationality == "Ethiopian"

if is_ethiopian and is_old_enough:
    print("you can vote")
elif not is_ethiopian and is_old_enough:
    print("apply for citizenship")
elif not is_ethiopian and not is_old_enough:
    print("no service")
