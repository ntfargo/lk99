import numpy as np
import matplotlib.pyplot as plt

class PhaseDiagram:
    def __init__(self):
        self.Tc = 104.8  # Critical temperature in °C
        self.temperatures = np.linspace(0, 150, 500)  # 0 to 150°C
        self.resistivities = self.calculate_resistivities()

    def calculate_resistivities(self):
        resistivities = np.zeros_like(self.temperatures)
        for i, T in enumerate(self.temperatures):
            if T < self.Tc:
                resistivities[i] = 0
            elif self.Tc <= T < 110:
                resistivities[i] = (T - self.Tc) * 0.2
            else:
                resistivities[i] = 1
        return resistivities

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.temperatures, self.resistivities, label='Resistivity vs. Temperature')
        plt.axvline(x=self.Tc, color='r', linestyle='--', label=f'Critical Temperature (Tc = {self.Tc}°C)')
        plt.title('Phase Diagram of LK-99')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Resistivity (Ohm.m)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def get_critical_temperature(self):
        return self.Tc