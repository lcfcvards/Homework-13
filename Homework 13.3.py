def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))


print(sum_range(1, 5))
print(sum_range(-8, 8))
print(sum_range(6, 4))
