# main.py
# so this is the runner for my dpll sat solver
# i made this to test on a few .cnf files i wrote by hand i dont exactly know if we 
#should test on the ones you ,mr teacher, gave us
# it shows time and result 



#I ALSO HAVE SOME EXPLANATIONS FOR WHAT I DID RIGHT BELOW


import time
from dpll_solver import dpll, parse_cnf

# this runs the actual test on 1 file
def run_experiment(file_path):
    print("testing on:", file_path)
    clauses, symbols = parse_cnf(file_path)

    start = time.time()
    result = dpll(clauses, symbols, [])
    end = time.time()

    if result:
        print("SATIISFIABLE")
    else:
        print("UNSATISFIABLE")

    print("took:", round((end - start)*1000, 3), "ms\n")

# files i tested on 
files = [
    "../data/test1.cnf",
    "../data/test2.cnf"
]

# loop through each one
for f in files:
    run_experiment(f)
