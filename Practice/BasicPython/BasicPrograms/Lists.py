# # Write a user-defined function to check if a number is present in the list or not.
# # If the number is present, return the position of the number. Print an appropriate
# # message if the number is not present in the list.
#
#
# # Assuming only numbers.
# def number_find(input_list, req_number):
#     position = 0  # Initializing.
#     for number in input_list:
#         if req_number == number:
#             return position
#         position += 1
#
#     print("The required number doesn't exist in the given list.")
#     return -1
#
#
# lists = [78, 0.987, "auth", 23]
#
# if type(lists) is list:
#     print("Yes")

stRecord = ['Raman', 'A-36', [56, 98, 99, 72, 69], 78.8]
stRecord[0] = "Raghav"
print(stRecord)
