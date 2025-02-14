import timeit
import statistics
import random
from typing import List, Callable, Tuple
from functions import (
    append_to_list, append_to_sublists, concatenate_to_tuple, concatenate_nested_tuple
)


def generate_random_containers(size: int) -> Tuple[list, list, tuple, tuple]:
    """Generate random containers of specified size"""
    base_list = [random.randint(1, 1000) for _ in range(size)]
    nested_list = [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(size // 2)]
    base_tuple = tuple(random.randint(1, 1000) for _ in range(size))
    nested_tuple = tuple((random.randint(1, 1000), random.randint(1, 1000)) for _ in range(size // 2))
    return base_list, nested_list, base_tuple, nested_tuple


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


def run_experiment(sizes: List[int], num_runs: int):
    """Run the timing experiment and print results"""
    print("\nDoubling Experiment Results:")
    print("-" * 100)
    print(f"{'Size':<12} {'List Append':>20} {'Nested List Append':>20} {'Tuple Concat':>20} {'Nested Tuple Concat':>20}")
    print("-" * 120)
    
    results = []
    for size in sizes:
        list_times = []
        nested_times = []
        tuple_times = []
        nested_tuple_times = []

        for _ in range(num_runs):
            base_list, nested_list, base_tuple, nested_tuple = generate_random_containers(size)
            # generate a list of elements to append (matching container size)
            elements_to_add = [random.randint(1, 1000) for _ in range(size)]

            # time each operation
            list_time = time_operation(append_to_list, base_list.copy(), elements_to_add)
            nested_time = time_operation(append_to_sublists, [lst.copy() for lst in nested_list], elements_to_add)
            tuple_time = time_operation(concatenate_to_tuple, base_tuple, elements_to_add)
            nested_tuple_time = time_operation(concatenate_nested_tuple, nested_tuple, elements_to_add)

            list_times.append(list_time)
            nested_times.append(nested_time)
            tuple_times.append(tuple_time)
            nested_tuple_times.append(nested_tuple_time)

        avg_list_time = statistics.mean(list_times)
        avg_nested_time = statistics.mean(nested_times)
        avg_tuple_time = statistics.mean(tuple_times)
        avg_nested_tuple_time = statistics.mean(nested_tuple_times)

        stddev_list_time = statistics.stdev(list_times) if len(list_times) > 1 else None
        stddev_nested_time = statistics.stdev(nested_times) if len(nested_times) > 1 else None
        stddev_tuple_time = statistics.stdev(tuple_times) if len(tuple_times) > 1 else None
        stddev_nested_tuple_time = statistics.stdev(nested_tuple_times) if len(nested_tuple_times) > 1 else None

        # print results in a formatted table
        print(f"{size:<12} {avg_list_time:>20.6f} {avg_nested_time:>20.6f} {avg_tuple_time:>20.6f} {avg_nested_tuple_time:>20.6f}")

        results.append([size, avg_list_time, avg_nested_time, avg_tuple_time, avg_nested_tuple_time, stddev_list_time, stddev_nested_time, stddev_tuple_time, stddev_nested_tuple_time])


if __name__ == "__main__":
    START_SIZE = 1000  # the starting size
    NUM_DOUBLES = 9    # number of times to double
    NUM_RUNS = 3

    sizes = generate_test_sizes(START_SIZE, NUM_DOUBLES)
    run_experiment(sizes, num_runs=NUM_RUNS)
