def sum(arr: list) -> int:
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])


print(sum([2, 4, 6, 2, 3, 3]))

