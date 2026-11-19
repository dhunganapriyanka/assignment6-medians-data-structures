
import random


# Deterministic selection using Median of Medians
def median_of_medians(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Divide the array into groups of five
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Choose a reliable pivot
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)

    # Divide values around the pivot
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    if k <= len(smaller):
        return median_of_medians(smaller, k)

    if k <= len(smaller) + len(equal):
        return pivot

    return median_of_medians(
        larger, k - len(smaller) - len(equal)
    )


# Randomized selection using Quickselect
def randomized_quickselect(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")

    # Select a random pivot
    pivot = random.choice(arr)

    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    if k <= len(smaller):
        return randomized_quickselect(smaller, k)

    if k <= len(smaller) + len(equal):
        return pivot

    return randomized_quickselect(
        larger, k - len(smaller) - len(equal)
    )


# Test both algorithms
if __name__ == "__main__":
    numbers = [12, 5, 8, 3, 15, 7, 5]
    k = 3

    print("Original Array:", numbers)
    print("Position (k):", k)

    print(
        "Median of Medians:",
        median_of_medians(numbers, k)
    )

    print(
        "Randomized Quickselect:",
        randomized_quickselect(numbers, k)
    )
