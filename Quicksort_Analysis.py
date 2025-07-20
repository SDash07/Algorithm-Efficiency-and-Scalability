# Required Libraries
import random
import time
import os
import matplotlib.pyplot as plt

# ----------------------------
# Randomized Quicksort
# ----------------------------
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# ----------------------------
# Deterministic Quicksort
# ----------------------------
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return deterministic_quicksort(less) + [pivot] + deterministic_quicksort(greater)

# ----------------------------
# Generate Test Datasets
# ----------------------------
def generate_datasets(sizes):
    datasets = []
    for size in sizes:
        datasets.append({
            "random": [random.randint(1, size) for _ in range(size)],
            "sorted": list(range(size)),
            "reverse": list(range(size, 0, -1)),
            "duplicates": [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
        })
    return datasets

# ----------------------------
# Time Comparison Plotter
# ----------------------------
def time_sorting_algorithms(sizes):
    datasets = generate_datasets(sizes)
    results = {"Randomized": [], "Deterministic": []}

    # Ensure the directory exists
    os.makedirs("results_plots", exist_ok=True)

    for i, size in enumerate(sizes):
        # Random dataset only for timing comparison
        data_random = datasets[i]["random"][:]

        # Time Randomized Quicksort
        start = time.time()
        randomized_quicksort(data_random[:])
        end = time.time()
        results["Randomized"].append(end - start)

        # Time Deterministic Quicksort
        start = time.time()
        deterministic_quicksort(data_random[:])
        end = time.time()
        results["Deterministic"].append(end - start)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results["Randomized"], label='Randomized Quicksort', marker='o')
    plt.plot(sizes, results["Deterministic"], label='Deterministic Quicksort', marker='s')
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Quicksort Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("results_plots/quicksort_comparison.png")
    plt.show()

# ----------------------------
# Run the Comparison
# ----------------------------
if __name__ == '__main__':
    sizes = [1000, 2000, 4000, 8000, 16000]
    time_sorting_algorithms(sizes)
