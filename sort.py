# a function to get the index of the smallest number
def find_smallest(arr):
    # save the first number as the smallest
    smallest = arr[0]
    # save the index as 0
    smallest_index = 0
    # run a loop to check the smallest number
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# function to sort the array passed
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # get the index of the smallest number
        smallest = find_smallest(arr)
        # append the smallest number to the new array after removing it from the old array
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
