# ppt_results.py

def get_ppt_results(method):
    if method == "BPNN-PID":
        return {
            "Tr": 290,
            "Ts": 357,
            "SteadyStateError": 0.0088,
            "Overshoot": 0.035,
            "RecoveryTime": 460,
            "Stability": "100%"
        }

    elif method == "WNN-PID":
        return {
            "Tr": 296,
            "Ts": 356,
            "SteadyStateError": 0.0152,
            "Overshoot": 0.0321,
            "RecoveryTime": 384,
            "Stability": "100%"
        }

    elif method == "MR-WNN-PID":
        return {
            "Tr": 263,
            "Ts": 331,
            "SteadyStateError": 0.0134,
            "Overshoot": 0.0000,
            "RecoveryTime": 477,
            "Stability": "100%"
        }
