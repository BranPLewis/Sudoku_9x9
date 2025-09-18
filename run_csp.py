from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking_with_h,solve_backtracking_without_h
import time

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    time_1 = time.time()
    for i, (sol,steps) in enumerate(solve_backtracking_without_h(csp), 1):
        any_sol = True
        print(f"\nSolution #{i}:")
        print(f"Steps on sol #{i}: {steps}")
        s = ""
        count = 0
        for value in sol.values():
            v = str(value)
            if count%9!=0:
                s += v
            else:
                s += "\n"
                s += v
            count += 1
        print(s)
    if not any_sol:
        print("No solutions.")
    time_2 = time.time()
    print("\nSolver without heuristics time: ",time_2-time_1,"\n")

    time_1 = time.time()
    for i, (sol,steps) in enumerate(solve_backtracking_with_h(csp), 1):
        any_sol = True
        print(f"\nSolution #{i}:")
        print(f"Steps on sol #{i}: {steps}")
        sorted_keys = sorted(sol.keys())
        new_map = {}
        for key in sorted_keys:
            new_map[key] = sol[key]
        s = ""
        count = 0
        for value in new_map.values():
            v = str(value)
            if count%9!=0:
                s += v
            else:
                s += "\n"
                s += v
            count += 1
        print(s)
    if not any_sol:
        print("No solutions.")
    time_2 = time.time()
    print("\nSolver with heuristics time: ",time_2-time_1,"\n")
