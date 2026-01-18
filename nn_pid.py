# nn_pid.py
import numpy as np

class NN_PID:
    def __init__(self):
        self.W1 = np.random.randn(3, 6) * 0.1
        self.W2 = np.random.randn(6, 3) * 0.1
        self.lr = 0.01

    def forward(self, x):
        self.h = np.tanh(x @ self.W1)
        out = self.h @ self.W2
        return out

    def update(self, x, error):
        grad_out = error
        dW2 = np.outer(self.h, grad_out)
        dW1 = np.outer(x, (1 - self.h**2) @ self.W2)

        self.W2 -= self.lr * dW2
        self.W1 -= self.lr * dW1
