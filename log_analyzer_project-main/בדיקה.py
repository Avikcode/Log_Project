data = [
    [3, 5, 7],
    [2, 11, 4],
    [1, 2],
    [15, 1]
]


if any(num > 10 for num in arr):

    for arr in data:
        if any(num > 10 for num in arr):
            arr.append("גדול")
        else:
            arr.append("רגיל")


