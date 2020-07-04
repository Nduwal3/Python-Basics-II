# Write a binary search function. It should take a sorted sequence and the item it is looking for.
#  It should return the index of the item if found. It should return -1 if the item is not found. 

def binary_search(sorted_list, low, high, item):
    if(item in sorted_list):
        mid_index = (high + low) // 2
        if (sorted_list[mid_index] == item ):
            return mid_index
        elif (sorted_list[mid_index] > item ):
            return binary_search(sorted_list, low , mid_index - 1, item)
        else:
            return binary_search(sorted_list, mid_index + 1, high,  item)
    else:
        return -1


sample_list = [1 , 9, 5, 3, 8, 2]
index = binary_search(sorted(sample_list), 0, len(sample_list), 9)
print(index)