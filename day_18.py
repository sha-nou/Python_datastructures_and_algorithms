import array

# Create the array
a = array.array("i", [1, 2, 3])

# Insert 4 at the end (corrected index)
a.append(4)


# Extend the array
a.extend([5, 6, 7, 8, 9, 10])
print("extended array", a)


# Function to rotate the array with a while loop
def rotate_array(arr):
    n = len(arr)
    k = 3
    while k<n:
        arr = arr[n - k :] + arr[: n - k]  
        print(f"Rotation {k + 1}: {arr}")  
        k += 1  

rotate_array(a)
