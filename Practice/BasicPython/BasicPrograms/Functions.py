# def my_func():
#     print("My first function in python!!!")
#
#
# Trying multiple return value function, with the help of tuples
def area_perimeter_rectangle(length, breadth):
    perimeter = 2 * (length + breadth)
    area = length * breadth
    return perimeter, area


L = int(input("Enter Length: "))
B = int(input("Enter Breadth: "))

Per, Area = area_perimeter_rectangle(L, B)
print("Perimeter =", Per, "\nArea =", Area)

# counter = 0
# print("counter =", counter)
#
#
# def increment_counter():
#     global counter
#     counter += 1
#
#
# increment_counter()
# print("counter after function call =", counter)

# print(chr(0x0001D54F))
# print(ord('𝕏'))
# print(ord(''))
# print(max(-1, 3, 50, 10))

# # Discount scheme for store XYZ
# def net_payable(shopping_amount, is_member=False):
#     final_price = shopping_amount
#     if shopping_amount >= 2000:
#         # 10 percent discount
#         final_price *= 90 / 100
#     elif 1000 <= shopping_amount < 2000:
#         # 8 percent discount
#         final_price *= 92 / 100
#     elif 500 <= shopping_amount < 1000:
#         # 5 percent discount
#         final_price *= 95 / 100
#
#     if is_member:
#         # 5 percent extra discount
#         final_price *= 95 / 100
#
#     return final_price

# def swapping(n1, n2):
#     n1 += 1
#     n2 += 2
#
#
# a = int(input())
# b = int(input())
#
# swapping(a, b)
#
# print(a, b)
