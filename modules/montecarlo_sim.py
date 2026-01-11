import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

def load_normalize(filename):
    # Loading numbers and normalizing it to be in range [0, 1]
    try:
        with open(filename, 'r') as f:
            data = [int(line.strip()) / 255.0 for line in f]
        return data
    except FileNotFoundError:
        print(f"Error: file {filename} was not found. ")
        return []
    
def monte_carlo(name, data):
    # Counting Pi using Monte Carlo simulation, return error history
    points_inside = 0
    total_points = 0
    errors = []

    # Numbers in pairs (x,y)
    for i in range(0, len(data), 2):
        x = data[i]
        y = data[i+1]

        # Circle equation x^2 + y^2 <= 1
        if x**2 + y**2 <= 1:
            points_inside += 1
        
        total_points += 1

        # Pi estimation = 4 * (inside/total)
        current_pi = 4 * (points_inside/total_points)

        # Count absolute error
        error = abs(current_pi - pi)
        errors.append(error)

    return errors

def plot_results(errors_q, errors_p, errors_lcg):
    
    plt.figure(figsize=(10,6))

    # x axis
    x_axis = range(1, len(errors_q) + 1)

    # Plot for quantum numbers
    plt.plot(x_axis, errors_q, label='ANU Quantum Numbers', color='blue', alpha=0.7, linewidth=1)

    # Plot for pseudorandom numbers
    plt.plot(x_axis, errors_p, label='Pseudorandom Numbers', color='red', alpha=0.7, linewidth=1, linestyle='--')

    # Plot for lcg numbers
    plt.plot(x_axis, errors_lcg, label='LCG Numbers', color='green', alpha=0.7, linewidth=1, linestyle='-.')

    plt.title("Monte Carlo Simulation")
    plt.xlabel("Number of points (tests)")
    plt.ylabel("Absolute error in Pi estimation (log scale)")
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', ls='-', alpha=0.4)

    print("Generating plot")
    #plt.show()

def check_len(file_1, file_2, file_3):
    min_len = min(len(file_1), len(file_2), len(file_3))

    if min_len % 2 != 0:
        min_len -= 1

    file_1 = file_1[:min_len]
    file_2 = file_2[:min_len]
    file_3 = file_3[:min_len]

    return file_1, file_2, file_3, min_len

