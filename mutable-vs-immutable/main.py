import timeit
import statistics
import random
from typing import List, Callable, Tuple
from functions import (
    append_to_list, append_to_sublists, concatenate_to_tuple
)


def generate_random_containers(size: int) -> Tuple[list, list, tuple]:
    """Generate random containers of specified size"""
    base_list = [random.randint(1, 1000) for _ in range(size)]

    nested_list = [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(size // 2)]

    base_tuple = tuple(random.randint(1, 1000) for _ in range(size))

    return base_list, nested_list, base_tuple


def generate_test_sizes(start_size: int, num_doubles: int) -> List[int]:
    """Generate list of sizes for doubling experiment"""
    return [start_size * (2 ** i) for i in range(num_doubles)]


def time_operation(func: Callable, input_data, elements, num_runs: int = 10, num_trials: int = 5) -> float:
    """Time an operation multiple times and return the median execution time."""
    times = [
        timeit.timeit(lambda: func(input_data.copy() if isinstance(input_data, list) else input_data, elements), number=num_runs)
        for _ in range(num_trials)
    ]
    return statistics.median(times) / num_runs 


def run_experiment(sizes: List[int]):
    """Run the timing experiment and print results"""
    print("\nDoubling Experiment Results:")
    print("-" * 100)
    print(f"{'Size':<12} {'List Append':>20} {'Nested List Append':>20} {'Tuple Concat':>20}")
    print("-" * 100)
    
    for size in sizes:
        base_list, nested_list, base_tuple = generate_random_containers(size)

        # generate a list of elements to append (matching container size)
        elements_to_add = [random.randint(1, 1000) for _ in range(size)]

        # time each operation
        list_time = time_operation(append_to_list, base_list.copy(), elements_to_add)
        nested_time = time_operation(append_to_sublists, [lst.copy() for lst in nested_list], elements_to_add)
        tuple_time = time_operation(concatenate_to_tuple, base_tuple, elements_to_add)

        # print results in a formatted table
        print(f"{size:<12} {list_time:>20.6f} {nested_time:>20.6f} {tuple_time:>20.6f}")


if __name__ == "__main__":
    START_SIZE = 500  # the starting size
    NUM_DOUBLES = 4    # number of times to double

    sizes = generate_test_sizes(START_SIZE, NUM_DOUBLES)
    run_experiment(sizes)
