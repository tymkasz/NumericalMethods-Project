import requests
import time
import os
import sys
import urllib3

# Disabling warning "Unverified HTTPS request" 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
ANU_API_URL = "https://qrng.anu.edu.au/API/jsonI.php"
batch_size = 1024 # Max for one request 
total_numbers = 500000 # Total amount of random numbers
filename = "data/anu_quantum_data.txt"

def fetch_quantum_numbers(total_count):

    # Function for downloading quatnum random numbers from ANU 

    all_numbers = []
    print(f"Starting to download {total_count} random numbers.")

    while len(all_numbers) < total_count:
        remaining = total_count - len(all_numbers)
        current_batch_size = min(remaining, batch_size) # How many to request for

        params = {'length': current_batch_size, 'type': 'uint8'} # Parameters for request

        try:
            print(f"Sending request for {current_batch_size} numbers.")

            response = requests.get(ANU_API_URL, params, timeout=10, verify=False) # Get response from ANU; if server will not respond in 10 sec, close session 
            if response.status_code == 200:
                data = response.json()

                if data['success']:
                    batch = data['data']
                    all_numbers.extend(batch)
                    print(f"Success! We have {len(all_numbers)}/{total_count}.")
                else:
                    print("API error")
            else:
                print(f"HTTP error: {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")

        if len(all_numbers) < total_count: # If it was not the last package
            print("Waiting for 120 seconds to unlock API limit.")
            for i in range(120, 0 , -1):
                # Using sys for clear remaining time presentation
                sys.stdout.write(f"\r Remains: {i} ")
                sys.stdout.flush() # Show what is in your bufor now!
                time.sleep(1)
            
            print("\r Procedure resumed")

    return all_numbers


def save_qrn_to_file(all_numbers, filename):
    with open(filename, 'w') as f:
        for num in all_numbers:
            f.write(f"{num}\n")
    print(f"Numbers saved into {filename}")

if __name__ == "__main__":
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        decision = input("Do you want to overwrite it? (y/n):")
        if decision.lower() != 'y':
            print("Canceled")
            exit()
    
    q_data = fetch_quantum_numbers(total_numbers)
    save_qrn_to_file(q_data, filename)



