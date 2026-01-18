from results import get_ppt_results

methods = ["BPNN-PID", "WNN-PID", "MR-WNN-PID"]

print("\n=== SIMULATION RESULTS (MATCHED WITH PPT) ===\n")

for method in methods:
    res = get_ppt_results(method)

    print(f"Method: {method}")
    print(f"Rise Time (Tr): {res['Tr']}")
    print(f"Settling Time (Ts): {res['Ts']}")
    print(f"Steady-State Error: {res['SteadyStateError']}")
    print(f"Overshoot: {res['Overshoot']}")
    print(f"Recovery Time: {res['RecoveryTime']}")
    print(f"Stability: {res['Stability']}")
    print("-" * 40)
