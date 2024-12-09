"""
NCERT Problems - Selected.
"""

'''
Write a program to read a list of n integers (positive as well as negative).Create two new
lists, one having all positive numbers and the other having all negative numbers from the
given list. Print all three lists.
'''

'''
n = int(input("Number of integers you want to input: "))

InputList = []

print("Enter the numbers, one by one:")
for i in range(n):
    InputList.append(int(input()))

PositiveIntegers = []
NegativeIntegers = []

for InputInt in InputList:
    if InputInt > 0:
        PositiveIntegers.append(InputInt)
    elif InputInt < 0:
        NegativeIntegers.append(InputInt)

print("Input List = ", InputList)
print("\t", "Positive Integers in the Input List =", PositiveIntegers)
print("\t", "Negative Integers in the Input List =", NegativeIntegers)
'''

# --------------------------------------------------------------------------------------------

'''
Write a program to read a list of n integers and find their median.
Note:
    The median value of a list of values is the middle one when they are arranged
    in order. If there are two middle values then take their average.
Hint: You can use an built-in function to sort the list
'''

'''
n = int(input("Number of integers you want to input: "))
assert n > 0

InputList = []

print("Enter the numbers, one by one:")
for i in range(n):
    InputList.append(int(input()))

InputList.sort()

if n % 2 == 0:
    Median = (InputList[int(n / 2) - 1] + InputList[int(n / 2)]) / 2
else:
    Median = InputList[int((n - 1) / 2)]

print("Median =", Median)
'''

# --------------------------------------------------------------------------------------------

'''
Read a list of n elements. Pass this list to a function which reverses this list in-place
without creating a new list.
'''

'''
def reverse_list_in_place(input_list):
    for index in range(0, int(len(input_list) / 2)):
        input_list[index], input_list[-index - 1] = input_list[-index - 1], input_list[index]


n = int(input("Number of elements you want to input: "))
assert n > 0

InputList = []

print("Enter the numbers, one by one:")
for i in range(n):
    InputList.append((input()))

print("Before =", InputList)
reverse_list_in_place(InputList)
print("After =", InputList)
'''
