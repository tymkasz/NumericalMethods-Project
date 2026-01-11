from modules import entropymodule
from modules import chisquaretest
from modules import montecarlo_sim
from modules import check_data_existence
import matplotlib.pyplot as plt


# Parameters
total_numbers = 500000
quantum_file = "data/anu_quantum_data.txt"
pseudonum_file = "data/pseudo_data.txt"
lcg_file = "data/lcg_data.txt"

check_data_existence.cde()

# Entropy test
print('\n')
print("ENTROPY TEST")
results = {}
results["ANU QUANTUM"] = entropymodule.analyze_dataset('ANU Qunatum Numbers', quantum_file)
results["Pseudo"] = entropymodule.analyze_dataset('Pseudorandom Numbers', pseudonum_file)
results["LCG"] = entropymodule.analyze_dataset('LCG Numbers', lcg_file)
entropymodule.plot_shannon_entropy(results)

# Chi^2 test
print("CHI SQUARE TEST")
#   Loading data
q_data_chi = chisquaretest.load_data(quantum_file)
p_data_chi = chisquaretest.load_data(pseudonum_file)
lcg_data_chi = chisquaretest.load_data(lcg_file)
#   Test
chisquaretest.chi_square_perform('ANU Qunatum Numbers', q_data_chi)
chisquaretest.chi_square_perform('Pseudorandom Numbers', p_data_chi)
chisquaretest.chi_square_perform('LCG Numbers', lcg_data_chi)

# Monte Carlo simulation
print("MONTE CARLO SIMULATION")
#   Loading and normalizing numbers
q_data_mc = montecarlo_sim.load_normalize(quantum_file)
p_data_mc = montecarlo_sim.load_normalize(pseudonum_file)
lcg_data_mc = montecarlo_sim.load_normalize(lcg_file)
#   Checking length
q_data_mc, p_data_mc, lcg_data_mc, min_len = montecarlo_sim.check_len(q_data_mc, p_data_mc, lcg_data_mc)

print(f"Analyzing for {min_len // 2} points")

#   Counting errors
err_quantum = montecarlo_sim.monte_carlo('Quantum random', q_data_mc)
err_pseudo = montecarlo_sim.monte_carlo('Pseudorandom', p_data_mc)
err_lcg = montecarlo_sim.monte_carlo('LCG', lcg_data_mc)
#   Plotting errors
montecarlo_sim.plot_results(err_quantum, err_pseudo, err_lcg)

plt.show()