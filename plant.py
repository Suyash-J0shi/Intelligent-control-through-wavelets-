# plant.py

class DiscretePlant:
    def __init__(self):
        self.y1 = 0.0
        self.y2 = 0.0

    def step(self, u):
        y = 1.8 * self.y1 - 0.81 * self.y2 + 0.1 * u
        self.y2 = self.y1
        self.y1 = y
        return y
