# # Positive and Negative
# For an input list of integers, we wish to know which positive numbers
# have corresponding negative numbers in the list.
# Example input:
# ```python
# [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
# ```
# Input can be in any order.
# Example return value:
# ```python
# [ 1, 3, 4 ]
# ```
# Because 1, 3, and 4 are the positive numbers that have corresponding
# negative numbers in the list.
# Return value can be in any order.
# Solve this problem with a hash table.
# Limits:
# * The input list can contain approximately 5,000,000 elements.

def has_negatives(a):
    # set up a dictionary
    # set up an answer array
    # run a check to see if there is a negative number coresponding to the value possibly with a variable
        # if it matches the value is appended into the array Need to make sure it is positive
    # if there isnt one there then the number is added to the dictionary
    # print answer array

    my_dict = {}
    answers = []

    for x in len(a):
        check = my_dict.get(0 - my_dict[x])
        if check:
            if x > 0:
                answers.append(x)
            else:
                answers.append(x * -1)
        else:
            my_dict[x] = x

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
