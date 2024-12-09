# Control Flow

# # Display the appropriate message as per the colour of signal at the road crossing.
# Colour = input("Enter the colour of the streetlight, in all caps: ")
#
# if Colour == "RED":
#     print("STOP")
# elif Colour == "YELLOW":
#     print("WAIT")
# elif Colour == "GREEN":
#     print("GO")
# else:
#     print("Give Proper Input.")

# # Write a program to create a simple calculator performing only four basic operations.
# FirstNum = int(input("Enter the First Number: "))
# SecondNum = int(input("Enter the First Number: "))
# Operator = input("Enter any of the operators +, -, * or /, which you would like to perform on the above numbers: ")
#
# if Operator == "+":
#     print(FirstNum + SecondNum)
# if Operator == "-":
#     print(FirstNum - SecondNum)
# if Operator == "*":
#     print(FirstNum * SecondNum)
# if Operator == "/":
#     print(FirstNum / SecondNum)
# else:
#     print("Wrong Operator Specified.")

# # Print 100 Numbers
# for i in range(1, 101):
#     print(i, end=" ")

# TestSet = {1, 3, 2, 3}
# print(type(TestSet))
# print(TestSet)
# for i in TestSet:
#     print(i)

# # WHILE LOOP
# while True:
#     print("Hi")

# for x in range(1, 4):
#     for y in range(2, 5):
#         if x * y > 10:
#             break
#         print(x * y)

# i = 0
# Sum = 0
# while i < 9:
#     if i % 4 == 0:
#         Sum = Sum + i
#     i = i + 2
# print(Sum)

# var = 7
# while var > 0:
#     print('Current variable value: ', var)
#     var = var - 1
#     if var == 3:
#         break
#     else:
#         if var == 6:
#             var = var - 1
#             continue
# print("Good bye!")

# # Print Table (1 to 10)
# Number = int(input("Enter the number whose table (from 1 to 10) is required: "))
#
# for i in range(1, 11):
#     print(Number, "x", i, "=", Number * i)

# Number = int(input())
# Max = Min = Number
#
# for i in range(1, 5):
#     Number = input()
#     if Number > Max:
#         Max = Number
#     elif Number < Min:
#         Min = Number
# print("Max = ", Max, ", Min = ", Min)

# InputString = input()
# Reverse = "".join(reversed(InputString))
# # for Letter in InputString:
# #     Reverse = Letter + Reverse
# if InputString == Reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

Magnitude = int(input())

print("")
print("Pattern 1:")
for i in range(1, Magnitude, 2):
    for p in range(int((Magnitude - i) / 2)):
        print(" ", end=" ")
    for q in range(i):
        print("*", end=" ")
    print("")
for i in range(Magnitude, 0, -2):
    for p in range(int((Magnitude - i) / 2)):
        print(" ", end=" ")
    for q in range(i):
        print("*", end=" ")
    print("")

# for i in range(1, Magnitude):
#     for p in range(Magnitude - i):
#         print(" ", end=" ")
#     for q in range(2 * i - 1):
#         print("*", end=" ")
#     print("")
# for i in range(Magnitude, 0, -1):
#     for p in range(Magnitude - i):
#         print(" ", end=" ")
#     for q in range(2 * i - 1):
#         print("*", end=" ")
#     print("")
#

print("")
print("Pattern 2:")
for i in range(1, Magnitude + 1):
    for p in range(Magnitude - i):
        print(" ", end=" ")
    for q in range(i, 1, -1):
        print(q, end=" ")
    for r in range(1, i + 1):
        print(r, end=" ")
    for s in range(Magnitude - i):
        print(" ", end=" ")
    print("")

print("")
print("Pattern 3:")
for i in range(Magnitude, 0, -1):
    for p in range(Magnitude - i):
        print(" ", end=" ")
    for q in range(1, i + 1):
        print(q, end=" ")
    print("")

print("")
print("Pattern 4:")
for i in range(1, Magnitude, 2):
    for p in range(int((Magnitude - i) / 2)):
        print(" ", end=" ")
    print("*", end=" ")
    for q in range(i - 2):
        print(" ", end=" ")
    if i != 1:
        print("*", end=" ")
    print("")
for i in range(Magnitude, 0, -2):
    for p in range(int((Magnitude - i) / 2)):
        print(" ", end=" ")
    print("*", end=" ")
    for q in range(i - 2):
        print(" ", end=" ")
    if i != 1:
        print("*", end=" ")
    print("")
