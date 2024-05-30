from typing import Optional

def max(arr: list, number_max: Optional[int] = None) -> int:
    if number_max is None:
        number_max = arr.pop()
    current = arr.pop()
    if current > number_max:
        number_max = current
    if arr:
        return max(arr, number_max)
    return number_max


print(max([1, 2, 3, 4, 5]))
    