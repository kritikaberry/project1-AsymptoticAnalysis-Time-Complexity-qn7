import random
import time
import matplotlib.pyplot as plt

# Function to compute the sum as per the nested loop logic (0-based indexing)
def compute_sum(a, b, c, n):
    Sum = 0
    for i in range(0, n):
        for j in range(i, n):
            for k in range(j * j, n):
                Sum += a[i] * b[j] * c[k]
    return Sum

# Generate random arrays a, b, c of size n
def generate_random_arrays(n, min_val=1, max_val=10):
    a = [random.randint(min_val, max_val) for _ in range(n)]
    b = [random.randint(min_val, max_val) for _ in range(n)]
    c = [random.randint(min_val, max_val) for _ in range(n)]
    return a, b, c

# Measure execution time of compute_sum for a given n
def time_compute_sum(n, min_val=1, max_val=10):
    a, b, c = generate_random_arrays(n, min_val, max_val)
    start = time.perf_counter_ns()        # high-resolution timer
    result = compute_sum(a, b, c, n)
    end = time.perf_counter_ns()
    time_ns = end - start                 # time in nanoseconds
    return time_ns, result

# Plot experimental times vs scaled theoretical O(n^2) curve
def plot_times(n_values, measured_times):
    theoretical_times = [n**2 for n in n_values]
    ref_index = len(n_values) // 2        # choosing midpoint as reference for scaling
    c = measured_times[ref_index] / theoretical_times[ref_index]  # scaling constant
    scaled_theoretical = [c * (n**2) for n in n_values]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, measured_times, marker='o', label='Experimental Time (ns)')
    plt.plot(n_values, scaled_theoretical, marker='x', label=f'Scaled Theoretical c·n² (c={c:.2f})')
    plt.xlabel('n (input size)')
    plt.ylabel('Time (nanoseconds)')
    plt.title('Experimental vs Scaled Theoretical Time for compute_sum')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Timing compute_sum")
    n_values = [10, 100, 1000, 10000, 100000]  # input sizes to test
    measured_times = []
    for n in n_values:
        print(f"Timing for n={n}...")
        t_ns, result = time_compute_sum(n)
        measured_times.append(t_ns)
        print(f"n={n}, Time taken={t_ns} ns, Result={result}")

    plot_times(n_values, measured_times)
