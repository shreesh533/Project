# arr = [5, 4, 3, 6, 7, 9, 2, 8]
# arr = [5, 3, 4, 9, 7]
arr = [5, 4, 3, 7, 9]
# arr = [5, 4, 3, 6, 7, 9, 2, 8]

list_of_difference = []
required_number = 12

for i in range(0, len(arr)):
    # If the iterating number exist in list of difference then we have first occurrence where
    # two numbers add up to required sum.
    if arr[i] in list_of_difference:
        print(required_number - arr[i], arr[i])
        break

    # Start making the array of difference between current number and required number.
    list_of_difference.append(required_number - arr[i])
