import random
import os 

total_numbers = 500000
filename = "data/pseudo_data.txt"

def generate_pseudorandom_numbers(total_numbers):

    # Function for generating pseudorandom numbers by random.randint() (Mersenne Twister) in range of 0 to 255 in uint8 format

    # Generating pseudorandom numbers 0-255 uint8
    print(f"Generating {total_numbers} pseudorandom numbers")
    all_numbers = [random.randint(0, 255) for _ in range(total_numbers)]

    return all_numbers

def save_pseudo_to_file(all_numbers, filename):
    with open(filename, 'w') as f:
        for num in all_numbers:
            f.write(f"{num}\n")
    print(f"Saved {len(all_numbers)} into {filename}.")

if __name__ == "__main__":
    # Overwriting file
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        decision = input("Do you want to overwrite it? (y/n): ")
        if decision.lower() != 'y':
            print("Canceled")
            exit()
    
    ps_data = generate_pseudorandom_numbers(total_numbers)
    save_pseudo_to_file(ps_data, filename)