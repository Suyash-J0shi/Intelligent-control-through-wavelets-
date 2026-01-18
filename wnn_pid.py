# wnn_pid.py
import numpy as np

def wavelet(x):
    return (1 - x**2) * np.exp(-x**2 / 2)

class WNN_PID:
    def __init__(self):
        self.W = np.random.randn(3, 6) * 0.1
        self.V = np.random.randn(6, 3) * 0.1
        self.lr = 0.008

    def forward(self, x):
        self.h = wavelet(x @ self.W)
        return self.h @ self.V

    def update(self, x, error):
        self.V -= self.lr * np.outer(self.h, error)
