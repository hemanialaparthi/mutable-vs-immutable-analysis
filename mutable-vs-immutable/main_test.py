import pytest
from main import generate_random_containers, generate_test_sizes, run_experiment, time_operation


def test_generate_random_containers():
    size = 10
    base_list, nested_list, base_tuple, nested_tuple = generate_random_containers(size)

    assert isinstance(base_list, list)
    assert isinstance(nested_list, list)
    assert isinstance(base_tuple, tuple)
    assert isinstance(nested_tuple, tuple)

    assert len(base_list) == size
    assert len(nested_list) == size // 2
    assert len(base_tuple) == size
    assert len(nested_tuple) == size // 2

    assert all(isinstance(item, int) and 1 <= item <= 1000 for item in base_list)
    assert all(isinstance(sublist, list) and len(sublist) == 2 for sublist in nested_list)
    assert all(isinstance(item, int) and 1 <= item <= 1000 for item in base_tuple)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in nested_tuple)


def test_generate_random_containers_empty():
    base_list, nested_list, base_tuple, nested_tuple = generate_random_containers(0)
    
    assert len(base_list) == 0
    assert len(nested_list) == 0
    assert len(base_tuple) == 0
    assert len(nested_tuple) == 0
    
    assert isinstance(base_list, list)
    assert isinstance(nested_list, list)
    assert isinstance(base_tuple, tuple)
    assert isinstance(nested_tuple, tuple)


def test_nested_list_structure():
    size = 20
    _, nested_list, _, _ = generate_random_containers(size)
    
    assert len(nested_list) == size // 2
    for sublist in nested_list:
        assert isinstance(sublist, list)
        assert len(sublist) == 2
        assert all(isinstance(item, int) and 1 <= item <= 1000 for item in sublist)


def test_nested_tuple_structure():
    size = 10
    _, _, _, nested_tuple = generate_random_containers(size)
    
    assert len(nested_tuple) == size // 2
    for subtuple in nested_tuple:
        assert isinstance(subtuple, tuple)
        assert len(subtuple) == 2
        assert all(isinstance(item, int) and 1 <= item <= 1000 for item in subtuple)


def test_generate_random_containers_different_values():
    size = 10
    containers1 = generate_random_containers(size)
    containers2 = generate_random_containers(size)
    
    assert containers1 != containers2
    
    for i in range(4):
        assert containers1[i] != containers2[i]
        
    assert any(item1 != item2 for item1, item2 in zip(containers1[0], containers2[0]))
    assert any(sublist1 != sublist2 for sublist1, sublist2 in zip(containers1[1], containers2[1]))
    assert any(item1 != item2 for item1, item2 in zip(containers1[2], containers2[2]))
    assert any(subtuple1 != subtuple2 for subtuple1, subtuple2 in zip(containers1[3], containers2[3]))


def test_generate_random_containers_odd_size():
    size = 11
    base_list, nested_list, base_tuple, nested_tuple = generate_random_containers(size)
    
    assert len(base_list) == size
    assert len(nested_list) == size // 2
    assert len(base_tuple) == size
    assert len(nested_tuple) == size // 2
    
    assert len(nested_list) == 5  # 11 // 2 = 5
    assert len(nested_tuple) == 5  # 11 // 2 = 5
    
    for sublist in nested_list:
        assert len(sublist) == 2
    
    for subtuple in nested_tuple:
        assert len(subtuple) == 2


def test_base_containers_size():
    size = 100
    base_list, _, base_tuple, _ = generate_random_containers(size)
    
    assert len(base_list) == size
    assert len(base_tuple) == size
    
    assert all(isinstance(item, int) and 1 <= item <= 1000 for item in base_list)
    assert all(isinstance(item, int) and 1 <= item <= 1000 for item in base_tuple)


def test_generate_test_sizes_large_values():
    start_size = 10**9  # 1 billion
    num_doubles = 30
    sizes = generate_test_sizes(start_size, num_doubles)
    
    assert len(sizes) == num_doubles
    assert sizes[0] == start_size
    assert sizes[-1] == start_size * (2 ** (num_doubles - 1))
    
    # Check that all sizes are unique and in ascending order
    assert len(set(sizes)) == num_doubles
    assert all(sizes[i] < sizes[i+1] for i in range(num_doubles - 1))
    
    # Check that no overflow occurred
    assert all(isinstance(size, int) for size in sizes)
    assert all(size > 0 for size in sizes)


def test_generate_test_sizes_doubling():
    start_size = 10
    num_doubles = 5
    sizes = generate_test_sizes(start_size, num_doubles)
    
    assert len(sizes) == num_doubles
    for i in range(1, len(sizes)):
        assert sizes[i] == sizes[i-1] * 2

def test_generate_test_sizes_zero_start():
    start_size = 0
    num_doubles = 5
    sizes = generate_test_sizes(start_size, num_doubles)
    
    assert len(sizes) == num_doubles
    assert all(size == 0 for size in sizes)


def test_time_operation_constant_time():
    def constant_time_function(input_data, elements):
        return input_data

    input_data = [1, 2, 3]
    elements = [4, 5, 6]
    execution_time = time_operation(constant_time_function, input_data, elements)

    assert isinstance(execution_time, float)
    assert execution_time > 0
    assert execution_time < 0.001  # Assuming constant time operation takes less than 1ms

def test_time_operation_expensive_function():
    def expensive_function(input_data, elements):
        return [sum(range(x)) for x in input_data]

    input_data = list(range(1000))
    elements = None
    execution_time = time_operation(expensive_function, input_data, elements)

    assert isinstance(execution_time, float)
    assert execution_time > 0
    assert execution_time < 1  # Assuming the expensive operation takes less than 1 second


def test_time_operation_with_exception():
    def raising_function(input_data, elements):
        raise ValueError("Test exception")

    input_data = [1, 2, 3]
    elements = [4, 5, 6]

    with pytest.raises(ValueError, match="Test exception"):
        time_operation(raising_function, input_data, elements)


def test_run_experiment_empty_sizes(capsys):
    run_experiment([])
    captured = capsys.readouterr()
    
    assert "Doubling Experiment Results:" in captured.out
    assert "Size" in captured.out
    assert "List Append" in captured.out
    assert "Nested List Append" in captured.out
    assert "Tuple Concat" in captured.out
    assert "Nested Tuple Concat" in captured.out
    assert len(captured.out.strip().split('\n')) == 4  # Header + 3 separator lines
