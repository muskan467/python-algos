def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the pivot element (usually the middle element)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)