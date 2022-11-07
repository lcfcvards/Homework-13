lst = [1, 4, 5, 8, -9]


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


change(lst)
print(lst)
