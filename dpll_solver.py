# dpll_solver.py
# eduard pepa - MPI 2025 UNU 
# so this is the file where i coded the dpll thing, which is like a basic SAT solver 
# tbh not that hard, just recursive guessing and checking if it works
# it’s not the fastest thing but it gets the job done on small formulas so yeah :)))

# this one checks if all clauses are true based on the current "assignment"
def is_satisfied(clauses, assignment):
    for clause in clauses:
        # if even one clause doesnt have at least 1 literal in the assignment, then no it’s not satisfied
        if not any(lit in assignment for lit in clause):
            return False
    return True  # all good everything satisfied

# this is the actual dpll recursive functn
def dpll(clauses, symbols, assignment):
    if is_satisfied(clauses, assignment):
        return assignment  # if already satisfied we done here :))9)

    if not symbols:
        return None  # no more vars to check and still not good ..fail

    p = symbols[0]      # take first var
    rest = symbols[1:]  # the rest to keep goin with

    # try assigning true and false basically
    for val in [p, -p]:
        new_assignment = assignment + [val]
        result = dpll(clauses, rest, new_assignment)
        if result is not None:
            return result  # if it worked return that thing

    return None  # if nothing works then no :((8

# here i parse the cnf file 
def parse_cnf(file_path):
    clauses = []
    symbols = set()

    with open(file_path, 'r') as f:
        for line in f:
            # ignore comments and the P line
            if line.startswith('c') or line.startswith('p'):
                continue
            clause = list(map(int, line.strip().split()))
            clause = [lit for lit in clause if lit != 0]  # remove that 0 at the end
            if clause:
                clauses.append(clause)
                for lit in clause:
                    symbols.add(abs(lit))  # store var number without sign

    return clauses, list(symbols)
