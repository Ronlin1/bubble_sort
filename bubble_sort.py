# Bubble Sort
def bubble_sort(a_list):
    # Setting Swapped to True to get the loop going and variable instantiating
    swapped = True
    while swapped:
        # This breaks the loop if we don't swap anything
        swapped = False
        for i in range(len(a_list) - 1):
            # compare list data and swap
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                # sets the flag to true if we swap
                swapped = True
    return a_list


# TEST
call_list = [23, 5, 667, 22, 4, 1, 56, 987, 34, 222, 70, 13, 19, 7]
print(f'My Unsorted List --> {call_list}')
call = bubble_sort(call_list)
print(f'My Bubble Sorted list ---> {call}')
