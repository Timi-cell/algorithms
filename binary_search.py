# binary search using python

def binary_search(array, search_item):
    # sort the array in case of scattered numbers
    array.sort()
    # setting where the search should start and end
    low = 0
    high = len(array) - 1
    # creating a while loop to check if the search_item is found in the array
    while low <= high:
        mid = int((low + high)/2)
        guess = array[mid]
        if guess == search_item:
            # return the index of the search_item
            return mid
        if guess > search_item:  # guess was too high
            # reducing the range of the search process from finish end
            high = mid - 1
        else:  # guess was too low
            # reducing the range of the search process from the start end
            low = mid + 1
            # return None if the search_item cannot be found in the array
    return None


my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_array, 7))
