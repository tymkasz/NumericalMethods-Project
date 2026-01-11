from . import qmodule
from . import pmodule
from . import lcgmodule
import os

quantum_file = "data/anu_quantum_data.txt"
pseudonum_file = "data/pseudo_data.txt"
lcg_file = "data/lcg_data.txt"
total_numbers = 500000

# Checking if files exist
def cde():
    # Quantum part
    if not os.path.exists(quantum_file):
        q_data = qmodule.fetch_quantum_numbers(total_numbers)
        qmodule.save_qrn_to_file(q_data, quantum_file)
    # Pseudorandom part
    if not os.path.exists(pseudonum_file):
        p_data = pmodule.generate_pseudorandom_numbers(total_numbers)
        pmodule.save_pseudo_to_file(p_data, pseudonum_file)
    # LCG part
    if not os.path.exists(lcg_file):
        state = int(input("Type a state of LCG: "))
        lcg_data = lcgmodule.lcg_generator(total_numbers, state)
        lcgmodule.save_lcg_to_file(lcg_data, lcg_file)