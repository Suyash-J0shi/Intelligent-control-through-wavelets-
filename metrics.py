# metrics.py
import numpy as np

def rise_time(y, ref):
    idx = np.where(y >= 0.9 * ref)[0]
    return idx[0] if len(idx) else None

def settling_time(y, ref, tol=0.02):
    for i in range(len(y)):
        if np.all(np.abs(y[i:] - ref) < tol * ref):
            return i
    return None

def overshoot(y, ref):
    return max(0, max(y) - ref)
