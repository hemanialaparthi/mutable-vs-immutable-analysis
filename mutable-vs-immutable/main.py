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
