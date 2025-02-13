def append_to_sublists(list_of_lists, element):
    for sublist in list_of_lists:
        if isinstance(sublist, list):
            sublist.append(element)
    return list_of_lists

# Example usage:
# nested_list = [[1, 2], [3, 4], [5, 6]]
# new_element = 99
# result = append_to_sublists(nested_list, new_element)
# print(result)


def append_to_list(input_list, element):
    """Appends new element to the input list"""
    input_list.append(element)
    return input_list


def concatenate_to_tuple(input_tuple, element):
    """Concatenates new element to the input tuple"""
    new_tuple = input_tuple + (element,)
    return new_tuple


def concatenate_nested_tuple(input_tuple, element):
    """Concatenates a new element to each tuple in a nested tuple"""
    result_tuple = ()
    for item in input_tuple:
        if isinstance(item, tuple):
            result_tuple += (item + (element,),)
    return result_tuple


