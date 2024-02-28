import timeit
import matplotlib.pyplot as plt
from decimal import Decimal

# Recursive method
def fibonacci_recursive(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Iterative method
def fibonacci_iterative(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Memoization method
def fibonacci_memoization(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memoize = {1: 0, 2: 1}
        for i in range(3, n + 1):
            memoize[i] = memoize[i - 1] + memoize[i - 2]
        return memoize[n]

# Using matrices
def fibonacci_matrix(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        F = [[1, 1],
             [1, 0]]
        power = matrix_power(F, n - 1)
        return power[0][0]

def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]

def matrix_power(M, power):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, M)
        M = matrix_multiply(M, M)
        power //= 2
    return result

# Binet's formula
def fibonacci_binet(n):
    phi1 = Decimal((1 - 5 ** 0.5) / 2)
    phi2 = Decimal((1 + 5 ** 0.5) / 2)
    return int((phi2 ** (n - 1) - phi1 ** (n - 1)) / Decimal(5 ** 0.5))

def fibonacci_dynamic(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

# Time complexity plotting
limited_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
larger_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

methods = [
   # ('Recursive', fibonacci_recursive),
    ('Iterative', fibonacci_iterative),
    ('Memoization', fibonacci_memoization),
    ('Matrix', fibonacci_matrix),
    ('Binet', fibonacci_binet),
    ('Dynamic', fibonacci_dynamic)
]

def plot_time_complexity(series, method, method_name):
    times = []
    for n in series:
        stmt = f"{method.__name__}({n})"
        setup = f"from __main__ import {method.__name__}"
        t = timeit.timeit(stmt, setup, number=10)
        times.append(t)
    plt.plot(series, times, label=method_name)
    plt.scatter(series, times)

def print_plot_time_complexity(series, method, method_name):
    print(method_name)
    #print("n", end="\t")
    # for n in series:
    #     print(n, end="\t")
    for n in series:
        stmt = f"{method.__name__}({n})"
        setup = f"from __main__ import {method.__name__}"
        t = timeit.timeit(stmt, setup, number=10)
        #print(n, " -> ")
        print(n, " -> ", round(t, 5), end="\t")
    print("\n")
# Plotting time complexity for each method in separate plots


plt.figure(figsize=(10, 6))
for method_name, method in methods:
    print_plot_time_complexity(larger_series, method, method_name)
    plot_time_complexity(larger_series, method, method_name)
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (s)')
    plt.title(f'{method_name} Fibonacci Function')
    plt.grid(True)
    plt.show()

# for method in methods:
#     #plot_time_complexity(limited_series, method, method.__name__)
#     print_plot_time_complexity(larger_series, method, method.__name__)





# import timeit
# import matplotlib.pyplot as plt
# from decimal import Decimal
#
#
# # Recursive method (used only with limited series)
# def fibonacci_recursive(n):
#     if n <= 0:
#         return "Input should be a positive integer"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#
# # Iterative method
# def fibonacci_iterative(n):
#     if n <= 0:
#         return "Input should be a positive integer"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n):
#             a, b = b, a + b
#         return b
#
# # Memoization method
# def fibonacci_memoization(n):
#     if n <= 0:
#         return "Input should be a positive integer"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#
#     memoize = {1: 0, 2: 1}
#     for i in range(3, n + 1):
#         memoize[i] = memoize[i - 1] + memoize[i - 2]
#     return memoize[n]
#
#
# # Using matrices
# def fibonacci_matrix(n):
#     if n <= 0:
#         return "Input should be a positive integer"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         F = [[1, 1],
#              [1, 0]]
#         power = matrix_power(F, n - 1)
#         return power[0][0]
#
# def matrix_multiply(A, B):
#     return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
#
# def matrix_power(M, power):
#     result = [[1, 0], [0, 1]]  # Identity matrix
#     while power > 0:
#         if power % 2 == 1:
#             result = matrix_multiply(result, M)
#         M = matrix_multiply(M, M)
#         power //= 2
#     return result
#
# # Binet's formula
# def fibonacci_binet(n):
#     phi1 = Decimal((1 - 5 ** 0.5) / 2)
#     phi2 = Decimal((1 + 5 ** 0.5) / 2)
#     return int((phi2 ** (n - 1) - phi1 ** (n - 1)) / Decimal(5 ** 0.5))
#
# # Dynamic programming
# def fibonacci_dynamic(n):
#     f = [0, 1]
#     for i in range(2, n + 1):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]
#
# # Time complexity plotting
# limited_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
# larger_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
#
# methods = {
#     #'Recursive': fibonacci_recursive,
#     'Iterative': fibonacci_iterative,
#     'Memoization': fibonacci_memoization,
#     'Matrix': fibonacci_matrix,
#     'Binet': fibonacci_binet,
#     'Dynamic': fibonacci_dynamic
# }
#
# # Time each method for both series
# times = {method: {'Limited': [], 'Larger': []} for method in methods}
#
# for method_name, method in methods.items():
#     for n in limited_series:
#         times[method_name]['Limited'].append(timeit.timeit(lambda: method(n), number=10))
#     for n in larger_series:
#         times[method_name]['Larger'].append(timeit.timeit(lambda: method(n), number=10))
#
# for method_name, timings in times.items():
#     plt.figure()  # Create a new figure for each method
#     plt.plot(limited_series, timings['Limited'], label=f'{method_name} (Limited)')
#     plt.plot(larger_series, timings['Larger'], label=f'{method_name} (Larger)')
#     plt.xlabel('N')
#     plt.ylabel('Time (s)')
#     plt.title(f'Time Complexity of {method_name} Fibonacci Algorithm')
#     plt.legend()
#     plt.show()
