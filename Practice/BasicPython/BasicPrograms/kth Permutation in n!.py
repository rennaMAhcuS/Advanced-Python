# To find: Given an index, now, we need to find the (rank)th Permutation of [1, 2, 3, ... , index]

index = int(input("Enter the index: "))
rank = int(input("Enter the rank: "))

# making a list of length n, in ascending order
main_list = []
for i in range(1, index + 1):
    main_list.append(i)


def factorial(p):
    p_fac = 1
    for j in range(1, p + 1):
        p_fac *= j
    return p_fac


# Main program
rank_list = []

rank_left = rank - 1

for k in range(1, index + 1):
    num = int(rank_left / (factorial(index - k)))
    rank_left = rank_left % factorial(index - k)
    rank_list.append(main_list[num])
    main_list.remove(main_list[num])

print(rank_list)
