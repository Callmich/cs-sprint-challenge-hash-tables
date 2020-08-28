
# # Intersections of Multiple Lists
# Find the intersection between multiple lists of integers.
# Do not use numpy or sets to solve this; use `dict` or hashtables, please.
# We're given a list of lists that contain integers:
# [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]
# And we need to compute the _intersection_, that is, numbers that exist in all lists.
# From the above input, the return value will be:
# [1, 2]

# Because those are the numbers that exist in all the lists.
# (Output can be in any order.)
# Limits:
# * There can be up to 10 lists in the list of lists.
# * The lists can contain up to roughly 1,000,000 elements each.

def intersection(arrays):
    # I'll need the length of our inital array
    # set up a dictionary to place each individual value and a counter for the value
    # run through the array of arrays
        # if a value is already in there then update the counter
        # else add to the dictionary
    
    # then I'll need a way to check the dictionary for all keys whose values match the length of the inital array
    
    match_num = len(arrays)
    my_dict = {}
    result = []

    # for arr in arrays:
    #     for x in range(len(arr)):
    #         if not my_dict.get(x):
    #             my_dict[x] = 1
    # ******** I just need to set up the inital dictionary with the first Array!


    first_array = arrays[0]
    rest_arrays = arrays[1:]

    for x in first_array:
        my_dict[x] = 1

    for arr in rest_arrays:
        for x in arr:
            if my_dict.get(x):
                my_dict[x] += 1

    for key in my_dict:
        if my_dict[key] == match_num:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
