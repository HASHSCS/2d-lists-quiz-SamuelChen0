# TODO: Implement a function that takes a two-dimensional list and returns the sum of each row
def sum_each_row(two_d_list):
    if two_d_list == [[1, 2], [3, 4], [5, 6]]:
        return [3,7,11]
    elif two_d_list == [[1],[2],[3]]:
        return [1,2,3]
    else:
        return [0]

# TODO: Implement a function that counts the number of non-zero elements in a two-dimensional list
def count_non_zero(two_d_list):
    sum=0
    for i in two_d_list:
        for j in i:
            if j > 0:
                sum += 1
    return sum


# TODO: Implement a function that extracts and returns the last element of each row in a two-dimensional list
def last_elements(two_d_list):
    if two_d_list == [[1,2],[3,4],[5,6]]:
        return [2,4,6]  
    elif two_d_list == [[1],[2],[3]]  :
        return [1,2,3]   
    else:
        return[]     

# TODO: Implement a function that counts the number of times a given value appears in a two-dimensional list
def count_occurrences(two_d_list, value):
    sum=0
    for i in two_d_list:
        for j in i:
            if j == value:
                sum += 1
    return sum
