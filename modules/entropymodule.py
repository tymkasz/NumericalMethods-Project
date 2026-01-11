import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt

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
    
def calculating_shannon_entropy(data):

    # Calculating Shannon entropy for number sequence (array)

    # If there is nothing in data array
    if not data:
        return 0.0
    
    # If data contains something (numbers), then:
    # 1. Count apperences of every numbers between 0 and 255 
    values, counts = np.unique(data, return_counts=True)

    # Show values of data
    print(f"Values: {values}")
    # Show how many times those values appeared
    print(counts)

    # 2. Count probabilities of every apperance
    # Thanks to numpy (vectorization) there is no need to write loops
    probabilities = counts/len(data)

    # 3. Counting Shannon entropy 
    # base=2 -> result in bits
    ent = entropy(probabilities, base=2)

    return ent

def analyze_dataset(name, filename):
    print(f"Analyzing {name}")
    data = load_data(filename)

    if data:
        ent = calculating_shannon_entropy(data)

        # Max entropy for byte 
        max_entropy = 8.0
        # Counting difference between ideal 
        diff = max_entropy - ent

        print(f"Number of samples: {len(data)}")
        print(f"Shannon entropy: {ent:.6f} bits")
        print(f"Loss to ideal entropy: {diff:.6f}")

        if diff < 0.01:
            print("High randomness")
        else:
            print("Low randomness")

        print("\n")
        return ent

    print("\n")
    return 0.0 # In case of lack of data

def plot_shannon_entropy(results):
    names = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(10,6))

    bars = plt.bar(names, values, color=['blue', 'red', 'green'])

    plt.ylim(7.99, 8.001)

    plt.axhline(y=8.0, color='black', linestyle='--', linewidth=1, label='Ideal (8 bits)')

    plt.title('Shannon entropy comparison')
    plt.ylabel('Entropy (bits)')
    plt.grid(axis='y', alpha=0.3)
    plt.legend(loc='lower left')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.0002, f'{height:.5f}', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    plt.tight_layout()
    #plt.show()



    
    

