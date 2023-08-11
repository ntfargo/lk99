import numpy as np
import matplotlib.pyplot as plt 

class PhaseDiagram:
    def __init__(self, synthesized_material):
        self.synthesized_material = synthesized_material
        self.temperatures = np.linspace(0, 150, 500) # 0 to 150°C
        self.resistivities = self.calculate_resistivities()

    def calculate_resistivities(self):
        resistivities = np.zeros_like(self.temperatures)
        for i, T in enumerate(self.temperatures):
            if T < 104.8:
                resistivities[i] = 0
            elif 104.8 <= T < 110:
                resistivities[i] = (T - 104.8) * 0.2 
            else:
                resistivities[i] = 1
        return resistivities

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.temperatures, self.resistivities, label='Resistivity vs. Temperature')
        plt.axvline(x=104.8, color='r', linestyle='--', label='Critical Temperature (Tc)')
        plt.title(f'Phase Diagram of {self.synthesized_material.name}')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Resistivity (Ohm.m)')
        plt.legend()
        plt.grid(True)
        plt.show()