def get_first_numbers_which_add(list_of_integers, start, end, required_sum):
    """
    Brute Force method.
    This function finds the least index of numbers which add.
    Start = 0
    end = 999(infinite)
    Let's say numbers at indexes a1 and b1 add to required_sum, now start_index becomes a1 and end_index becomes b1.
    If in next iteration we find a2 and b2 adds up to required_sum and b2 < b1 then b2 appears before b1.
    So start_index = a2 and end_index = b2. And so on..
    """
    end_index = 999
    start_index = 0
    for i in range(start, end):
        for j in range(i, end):
            if list_of_integers[i] + list_of_integers[j] == required_sum:
                if j < end_index:
                    end_index = j
                    start_index = i

    print(list_of_integers[start_index], list_of_integers[end_index])


# list_of_integers = [5, 3, 4, 9, 7]
# list_of_integers = [5, 4, 3, 7, 9]
list_of_integers = [5, 4, 3, 6, 7, 9, 2, 8]
required_sum = 11
get_first_numbers_which_add(list_of_integers, 0, len(list_of_integers), required_sum)