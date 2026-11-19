
import random
import time
import statistics

from selection_algorithms import (
    median_of_medians,
    randomized_quickselect
)


def measure_time(algorithm, data, k):
    times = []

    # Run each test five times
    for _ in range(5):
        start = time.perf_counter()

        result = algorithm(data.copy(), k)

        end = time.perf_counter()

        # Check that the result is correct
        assert result == sorted(data)[k - 1]

        times.append(end - start)

    return statistics.mean(times)


def run_performance_tests():
    sizes = [1000, 5000, 10000]

    print("Selection Algorithm Performance Analysis")
    print("-" * 75)

    print(
        f"{'Size':<10} {'Dataset':<15} "
        f"{'Median of Medians':<22} {'Quickselect':<15}"
    )

    print("-" * 75)

    for size in sizes:
        random_data = [
            random.randint(1, size * 10)
            for _ in range(size)
        ]

        datasets = {
            "Random": random_data,
            "Sorted": sorted(random_data),
            "Reverse": sorted(random_data, reverse=True)
        }

        for name, data in datasets.items():
            k = (len(data) + 1) // 2

            deterministic_time = measure_time(
                median_of_medians, data, k
            )

            randomized_time = measure_time(
                randomized_quickselect, data, k
            )

            print(
                f"{size:<10} {name:<15} "
                f"{deterministic_time:<22.6f} "
                f"{randomized_time:<15.6f}"
            )


if __name__ == "__main__":
    run_performance_tests()
