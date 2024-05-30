def len(arr: list, lens: int = 0) -> int:
    if not arr:
        return lens
    lens += 1
    return len(arr[1:], lens)


print(len([1, 2, 3, 4, 5]))