# classical_pid.py

class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.e1 = 0.0
        self.e2 = 0.0
        self.u = 0.0

    def update(self, e):
        du = (
            self.kp * (e - self.e1)
            + self.ki * e
            + self.kd * (e - 2 * self.e1 + self.e2)
        )
        self.u += du
        self.e2 = self.e1
        self.e1 = e
        return self.u
