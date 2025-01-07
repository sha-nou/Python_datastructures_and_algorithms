import array

a = array.array("i", [1, 2, 3])
b = array.array("i", [11, 12, 13])
a.insert(4, 4)
a.index(1)
a += b
count = a.count(1)
a.extend([5, 6, 7, 8, 9, 10])
print(a)


def swap(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        arr[n - 1] = temp
        i += 1


swap(a, 5)
print(a)


def reverse_array(end, start, arr):
    reverse_order = end - start + 1
    count = 0
    while (reverse_order) // 2 != count:
        arr[start + count], arr[end - count] = arr[end - count], arr[start + count]
        count += 1
        return arr


def rotate_arr(arr, size, d):
    start = 0
    end = size - 1
    arr = reverse_array(start, end, arr)

    start = size - d
    end = size - 1
    arr = reverse_array(start, end, arr)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
size = 8
d = 1
print(arr)

if d <= size:
    print(rotate_arr(arr, size, d))
else:
    d = d % size
    print(rotate_arr(arr, size, d))
