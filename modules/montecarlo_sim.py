import matplotlib.pyplot as plt
import numpy as np
import os

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

def plot_distribution_2d(name, data, output_dir='images'):

    print(f"Generating 2D plot for {name}")

    np_data = np.array(data)

    # If data is odd, slice the last character to make data even
    if len(np_data) % 2 != 0:
        np_data = np_data[:-1]

    # -1 automates shape, 2 dimensional vectors
    points = np_data.reshape(-1, 2)

    # Give me 0th index of all rows from points -> x
    x = points[:, 0]
    # Give me 1st index of all rows from points -> y
    y = points[:, 1]

    r_squared = x**2 + y**2

    point_inside = r_squared <= 1

    # Points inside
    x_in, y_in = x[point_inside], y[point_inside]
    # Points outside
    x_out, y_out = x[~point_inside], y[~point_inside]

    # Drawing
    plt.figure(figsize=(8,8))
    plt.scatter(x_in, y_in, color='green', s=0.5, alpha=0.5, label='Inside')
    plt.scatter(x_out, y_out, color='red', s=0.5, alpha=0.5, label='Outside')

    # Circular arc
    theta = np.linspace(0, pi/2, 200)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', linewidth=2, alpha=0.7)

    # Plot appearance
    plt.title(f'2D points distribution: {name}\n(Number of points: {len(points)})')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    safe_name = name.replace(" ", "_").lower()
    filename = os.path.join(output_dir, f"2d_{safe_name}.png")

    plt.savefig(filename, dpi=150)
    print(f"Plot saved to {filename}")
    
def plot_multiple_runs(results_dict, title="Comparsion of Monte Carlo simulations"):
    """
    Draws multiple error plots in a single figure.
    results_dict: dictionary in the format {'Series Name': [error_list], ...}
    """
    plt.figure(figsize=(12, 7))

    colors = ['blue', 'cyan', 'navy', 'purple', 'magenta'] # Color palette for the series
    
    # We iterate through the dictionary and draw each series
    for i, (label, errors) in enumerate(results_dict.items()):
        # We select the color cyclically (if there are more series than colors)
        color = colors[i % len(colors)]
        x_axis = range(1, len(errors) + 1)
        
        plt.plot(x_axis, errors, label=label, color=color, alpha=0.6, linewidth=0.8)

    plt.title(title)
    plt.xlabel("Number of points (tests)")
    plt.ylabel("Absolute error of Pi estimation (log scale)")
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which='both', ls='-', alpha=0.3)

    output_file = f"images/comparison_{title.replace(' ', '_').lower()}.png"
    plt.savefig(output_file, dpi=150)
    print(f"Comparison chart saved to: {output_file}")
    # plt.show() # Optionally, if you want to see
    plt.close()









