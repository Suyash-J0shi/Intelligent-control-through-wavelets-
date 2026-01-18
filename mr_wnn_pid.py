# mr_wnn_pid.py
import numpy as np
from wnn_pid import wavelet

class MR_WNN_PID:
    def __init__(self):
        self.W = np.random.randn(3, 6) * 0.1
        self.V = np.random.randn(6, 3) * 0.1
        self.lr = 0.005
        self.a1, self.a2, self.b1 = 1.8, -0.81, 0.1
        self.y1 = 0
        self.y2 = 0

    def predict(self, u):
        y_pred = self.a1 * self.y1 + self.a2 * self.y2 + self.b1 * u
        self.y2 = self.y1
        self.y1 = y_pred
        return y_pred

    def forward(self, x):
        self.h = wavelet(x @ self.W)
        return self.h @ self.V

    def update(self, x, error):
        self.V -= self.lr * np.outer(self.h, error)
