import numpy as np
from scipy.stats import chisquare

max_range = 256

def load_data(filename):
    # Loading data (numbers) from file into arrays
    try:
        with open(filename, 'r') as f:
            # Loading numbers, deleting white spaces and formating into int
            data = [int(line.strip()) for line in f]
        return data
    except FileNotFoundError:
        print(f"Error: file {filename} was not found. ")
        return []
    
def chi_square_perform(name, data):

    # Loading length of data file
    n = len(data)
    if n == 0: return

    # 1. Count apperances of numbers between 0 and 255
    # Histogram -> also count number that did not appear
    observed_count, _ = np.histogram(data, bins=range(257))

    # 2. Count number of expected count for every number
    expected_count = n/max_range
    expected_counts = [expected_count] * max_range

    # 3. Perform chi square test
    chi2_val, p_val = chisquare(f_obs=observed_count, f_exp=expected_counts)

    print(name)
    print(f"Number of samples: {n}")
    print(f"Chi Square statistics: {chi2_val:.6f}")
    print(f"p-value: {p_val:.6f}")

    # NIST interpretation (significance level - alpha = 0.01)
    alpha = 0.01
    if p_val >= alpha:
        print("Result: positive. Distribution seems random.")
        print(f"    No need to reject hypothesis (p >= {alpha})")
    if p_val < alpha:
        print("Result: negative. Distribution seems pseudorandom.")
        print(f"    Distribution too little or too regularly (p < {alpha})")

    print("\n")

