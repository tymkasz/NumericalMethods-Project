import os

total_numbers = 500000
filename = 'data/lcg_data.txt'

def lcg_generator(n, state):

    # c and m are coprime
    # All the prime factors of m divide a-1 
    # If 4 divides m, then 4 divides a-1
    a = 1664525
    c = 1013904223
    # The prime factor of m is 2
    # So c is odd
    m = 2**32

    all_numbers = []

    # Generating numbers
    for _ in range(n):
        state = (a * state + c) % m
        val_byte = state >> 24

        all_numbers.append(val_byte)

    return all_numbers

def save_lcg_to_file(all_numbers, filename):
    with open(filename, 'w') as f:
        for num in all_numbers:
            f.write(f"{num}\n")
    print(f"Saved {len(all_numbers)} integers into {filename}.")

if __name__ == "__main__":
    # Overwriting file
    if os.path.exists(filename):
        print(f"File {filename} exists.") 
        decision = input("Do you want to overwrite it? (y/n): ")
        if decision.lower() != 'y':
            print("Canceled")
            exit()
    
    state = int(input("Type a state of LCG: "))
    lcg_data = lcg_generator(total_numbers, state)
    save_lcg_to_file(lcg_data, filename)