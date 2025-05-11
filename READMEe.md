# SAT Solver (DPLL) — MPI(L)2025 Project

## 👋 Author
Eduard Pepa

Hey! This is my SAT solver project I worked on for the MPI(L) course in 2025. It’s a basic implementation of a SAT checker using the DPLL algorithm, and I coded everything in Python.



##  What the project does

This solver reads logic expressions in CNF format (those weird .cnf files), and it figures out if there’s any way to assign values like True/False to the variables to make the whole thing true.

The DPLL algorithm goes through the variables recursively and tries both options. It stops if the formula is satisfied.



##  Folder overview

```
SATProject/
├── code/
│   ├── dpll_solver.py   # Where the logic lives
│   └── main.py          # Loads input and runs tests
├── data/
│   ├── test1.cnf        # First test (2 clauses)
│   └── test2.cnf        # Second test (3 clauses)
└── paper/
    └── SATpaper.tex     # Full report, written in LaTeX
```



## Sample output

```
testing on: test1.cnf
SATISFIABLE
Time: 1.23 ms

testing on: test2.cnf
SATISFIABLE
Time: 2.45 ms
```



## What I learned doing this

- How SAT problems work (and what CNF even is)
- How to use recursion in practice
- How to parse structured files like .cnf
- How to test things cleanly without overcomplicating it

It was a bit tricky to debug recursion and understand how the CNF format works at first, but I’m glad I got it working.

---

##  Final thoughts

This was written entirely by me, no libraries or copy-paste tricks. The goal was to understand the logic and actually make something that works. It may be simple, but it does the job.

Thanks for checking it out!

