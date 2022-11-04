# matrix = [
# [1  ,4,  7,     12,     15,     1000],
# [2  ,5,  19,    31,     32,     1001],
# [3  ,8,  24,    33,     35,     1002],
# [40 ,41, 42,    43,     44,     1003],
# [99 ,100,103,   106,    128,    1004]
# ]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]


def find_elem(my_matrix, target):
    for i in range(len(my_matrix)):
        try:
            return [i, my_matrix[i].index(target)]
        except ValueError:
            continue
    return [-1, -1]


print(find_elem(matrix, 44))


