# cosas.py
import numpy as np
import utils
import subprocess
import sys
import csv
import statistics
from pulp import *

############################
# Arguments. To run this code, run "python compare_restrictions.py <Robinson space size> <number of iterations>"
############################
if len(sys.argv) < 3:
    print("Use: python compare_restrictions.py <Robinson space size> <number of iterations>")
    sys.exit(1)

n_size = int(sys.argv[1])
n_iter = int(sys.argv[2])

############################
# Store results
############################
results = []

############################
# Main loop
############################
for rep in range(n_iter):
    # Generate matrix using Laurent's Robinson space generator
    subprocess.call(["/usr/bin/Rscript", "create_Robinson.r", str(n_size)])
    input_matrix = np.genfromtxt("random_robinson_matrix.csv", delimiter=',')
    
    # Compute distance matrix
    distance_matrix = input_matrix.max() - input_matrix

    # Compute left/right centers
    max_closer = utils.compute_max_closer(distance_matrix)
    
    ##########################
    # Reduced problem
    ##########################
    red_problem = LpProblem("Aux_problem", LpMinimize)
    red_distance = LpVariable.dicts("aux_distance", range(n_size), cat='Continuous')
    red_leg = LpVariable.dicts("aux_leg", range(n_size), cat='Continuous')
    red_problem += 0  # dummy target

    two_points = [(i, j) for i in range(n_size) for j in range(n_size) if i != j]

    for (i, j) in two_points:
        if i < j:
            if (i == j-1) or ((max_closer[i, j-1] != max_closer[i, j]) and ((i == 0) or (max_closer[i-1, j] != max_closer[i, j]))):
                red_problem += red_distance[i] + red_distance[j] - 2*red_distance[max_closer[i, j]] - red_leg[i] + red_leg[j] >= 1
        elif i > j:
            if (i == j+1) or ((max_closer[i, j+1] != max_closer[i, j]) and ((i == (n_size-1)) or (max_closer[i+1, j] != max_closer[i, j]))):
                red_problem += -red_distance[i] - red_distance[j] + 2*red_distance[max_closer[i, j]] - red_leg[i] + red_leg[j] >= 1

    #Count the amount of constraints in the reduced problem
    red_constraints = len(red_problem.constraints)

    ##########################
    # Main problem
    ##########################
    problem = LpProblem("Main_problem", LpMinimize)

    distance = LpVariable.dicts("distance", range(n_size), cat='Continuous', lowBound=0)
    leg = LpVariable.dicts("leg", range(n_size), cat='Continuous', lowBound=0)

    problem += lpSum([0*leg[i] for i in range(n_size)])

    for (i, j) in two_points:
        if (i < j-1):
            problem += distance[i] + distance[j] - 2*distance[max_closer[i, j]] - leg[i] + leg[j] >= 1
        elif (i > j+1):
            problem += -distance[i] - distance[j] + 2*distance[max_closer[i, j]] - leg[i] + leg[j] >= 1
        elif (i == j-1):
            problem += distance[i] + distance[j] - 2*distance[max_closer[i, j]] - leg[i] + leg[j] >= 1
        elif (i == j+1):
            problem += -distance[i] - distance[j] + 2*distance[max_closer[i, j]] - leg[i] + leg[j] >= 1

    main_constraints = len(problem.constraints)

    #Store results
    results.append({
        "iteration": rep + 1,
        "size": n_size,
        "red_constraints": red_constraints,
        "main_constraints": main_constraints
    })

############################
# Save results into a CSV
############################
results_filename = f"results_{n_size}.csv"
with open(results_filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

############################
# Global stats
############################
red_constraints_list = [r["red_constraints"] for r in results]
main_constraints_list = [r["main_constraints"] for r in results]

summary = {
    "size": n_size,
    "n_iter": n_iter,
    "red_constraints_mean": statistics.mean(red_constraints_list),
    "red_constraints_std": statistics.pstdev(red_constraints_list),
    "main_constraints_mean": statistics.mean(main_constraints_list),
    "main_constraints_std": statistics.pstdev(main_constraints_list)
}

# Save summary in a CSV
summary_filename = f"summary_{n_size}.csv"
with open(summary_filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=summary.keys())
    writer.writeheader()

    writer.writerow(summary)
