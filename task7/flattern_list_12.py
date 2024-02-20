#  Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])
nested_list = [1, [2, 3], [4, [5, 6]]]

def flatten(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result = result + flatten(i)
        else:
            result.append(i)
    return result

new_l = flatten(nested_list)
print(new_l)