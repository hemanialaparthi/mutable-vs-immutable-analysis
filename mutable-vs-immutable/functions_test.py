import pytest
import time
from functions import append_to_sublists, concatenate_to_tuple, concatenate_nested_tuple


def test_append_to_all_sublists():
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    element = 99
    result = append_to_sublists(list_of_lists, element)
    assert result == [[1, 2, 99], [3, 4, 99], [5, 6, 99]]
    assert result is list_of_lists  # Check if the original list is modified


def test_append_to_nested_sublists():
    nested_list = [[1, 2], [3, [4, 5]], [6, 7]]
    element = 99
    result = append_to_sublists(nested_list, element)
    assert result == [[1, 2, 99], [3, [4, 5], 99], [6, 7, 99]]
    assert result is nested_list  # Check if the original list is modified


def test_append_to_large_list():
    large_list = [[i] for i in range(100000)]
    element = 99
    start_time = time.time()
    result = append_to_sublists(large_list, element)
    end_time = time.time()
    execution_time = end_time - start_time
    
    assert len(result) == 100000
    assert all(sublist[-1] == element for sublist in result)
    assert execution_time < 1.0  # Ensure execution time is less than 1 second
    assert result is large_list  # Check if the original list is modified


def test_append_list_element():
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    element = [99, 100]
    result = append_to_sublists(list_of_lists, element)
    assert result == [[1, 2, [99, 100]], [3, 4, [99, 100]], [5, 6, [99, 100]]]
    assert result is list_of_lists  # Check if the original list is modified


def test_append_different_data_types():
    list_of_lists = [[1, 2], [3, 4], [5, 6]]
    elements = [99, "string", 3.14, True, None]
    for element in elements:
        result = append_to_sublists(list_of_lists, element)
    assert result == [[1, 2, 99, "string", 3.14, True, None],
                      [3, 4, 99, "string", 3.14, True, None],
                      [5, 6, 99, "string", 3.14, True, None]]
    assert result is list_of_lists  # Check original list is modified


def test_concatenate_empty_tuple():
    empty_tuple = ()
    element = 42
    result = concatenate_to_tuple(empty_tuple, element)
    assert result == (42,)
    assert isinstance(result, tuple)
    assert result is not empty_tuple  # Check that a new tuple is created


def test_concatenate_non_empty_tuple():
    input_tuple = (1, 2, 3)
    element = 4
    result = concatenate_to_tuple(input_tuple, element)
    assert result == (1, 2, 3, 4)
    assert result is not input_tuple  # Check that a new tuple is created
    assert input_tuple == (1, 2, 3)  # Check that the original tuple is not modified


def test_concatenate_tuple_with_float():
    input_tuple = (1, 2, 3)
    element = 4.5
    result = concatenate_to_tuple(input_tuple, element)
    assert result == (1, 2, 3, 4.5)
    assert isinstance(result, tuple)
    assert isinstance(result[-1], float)
    assert result is not input_tuple  # Check that a new tuple is created
    assert input_tuple == (1, 2, 3)  # Check that the original tuple is not modified


def test_concatenate_tuple_with_integer():
    input_tuple = (1, 2, 3)
    element = 4
    result = concatenate_to_tuple(input_tuple, element)
    assert result == (1, 2, 3, 4)
    assert isinstance(result, tuple)
    assert result is not input_tuple  # Check that a new tuple is created
    assert input_tuple == (1, 2, 3)  # Check that the original tuple is not modified


def test_concatenate_large_tuple():
    large_tuple = tuple(range(10000))
    element = 10000
    result = concatenate_to_tuple(large_tuple, element)
    assert len(result) == 10001
    assert result[-1] == element
    assert result[:-1] == large_tuple
    assert result is not large_tuple  # Check that a new tuple is created
    assert isinstance(result, tuple)


def test_concatenate_nested_tuple_with_non_tuple_iterables():
    input_tuple = ((1, 2), [3, 4], (5, 6), {7, 8})
    element = 99
    result = concatenate_nested_tuple(input_tuple, element)
    assert result == ((1, 2, 99), (5, 6, 99))
    assert isinstance(result, tuple)
    assert all(isinstance(item, tuple) for item in result)
    assert len(result) == 2
    assert input_tuple == ((1, 2), [3, 4], (5, 6), {7, 8})  # Check that the original tuple is not modified


def test_concatenate_nested_tuple_with_repeated_tuples():
    input_tuple = ((1, 2), (3, 4), (1, 2), (5, 6), (3, 4))
    element = 99
    result = concatenate_nested_tuple(input_tuple, element)
    assert result == ((1, 2, 99), (3, 4, 99), (1, 2, 99), (5, 6, 99), (3, 4, 99))
    assert isinstance(result, tuple)
    assert all(isinstance(item, tuple) for item in result)
    assert len(result) == 5
    assert input_tuple == ((1, 2), (3, 4), (1, 2), (5, 6), (3, 4))  # Check that the original tuple is not modified


def test_concatenate_nested_tuple_with_different_data_types():
    input_tuple = ((1, 2.5), ("hello", True), (False, None))
    element = 99
    result = concatenate_nested_tuple(input_tuple, element)
    assert result == ((1, 2.5, 99), ("hello", True, 99), (False, None, 99))
    assert isinstance(result, tuple)
    assert all(isinstance(item, tuple) for item in result)
    assert len(result) == 3
    assert input_tuple == ((1, 2.5), ("hello", True), (False, None))  # Check that the original tuple is not modified
