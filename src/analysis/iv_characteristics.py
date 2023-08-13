import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
import h5py
import pandas as pd
from simulation.phase import PhaseDiagram

class IVCharacteristics:
    def __init__(self, Ic=1.0, n=30, Vc=0.001):
        self.Ic = Ic
        self.n = n
        self.Vc = Vc
        self.phase_diagram = PhaseDiagram()
        self.Tc = self.phase_diagram.get_critical_temperature()
        self.energy_gap = self.calculate_energy_gap()

    def iv_curve(self, V):
        # return self.Ic * (np.abs(V) / self.Vc) ** (1/self.n)
        return self.Ic * np.tanh(V / self.Vc)

    def generate_iv_data(self, V_range):
        return self.iv_curve(V_range)

    def export_data(self, V, I, filename, format='h5'):
        if not os.path.exists('./data/'):
            os.makedirs('./data/') 
        filename = os.path.join('./data/', filename) 
        if format == 'h5':
            with h5py.File(filename, 'w') as f:
                f.create_dataset('Voltage', data=V)
                f.create_dataset('Current', data=I)
        elif format == 'csv':
            df = pd.DataFrame({'Voltage': V, 'Current': I})
            df.to_csv(filename, index=False)

    def import_data(self, filename, format='h5'):
        if format == 'h5':
            with h5py.File(filename, 'r') as f:
                V = f['Voltage'][:]
                I = f['Current'][:]
        elif format == 'csv':
            df = pd.read_csv(filename)
            V = df['Voltage'].values
            I = df['Current'].values
        return V, I

    def fit_data(self, V_exp, I_exp):
        params, _ = curve_fit(self.iv_curve, V_exp, I_exp)
        self.Ic, self.n, self.Vc = params
        return params
    
    def calculate_energy_gap(self):
        kB = 8.617333262145e-5  # Boltzmann constant in eV/K
        return 1.76 * kB * self.Tc

    def plot(self, V, I, V_exp=None, I_exp=None):
        """Visualize the I-V curve."""
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))
        V_mV = V * 1000
        I_mA = I * 1000
        plt.title(f'I-V Characteristics of LK-99 at Tc = {self.Tc}°C, Energy Gap = {self.energy_gap:.6f} eV')
        if V_exp is not None and I_exp is not None:
            V_exp_mV = V_exp * 1000
            I_exp_mA = I_exp * 1000
            plt.plot(V_exp_mV, I_exp_mA, '-', label='Experimental Data', color='red')
        
        plt.title('I-V Characteristics of LK-99')
        plt.xlabel('Voltage (mV)')
        plt.ylabel('Current (mA)')
        plt.legend()
        plt.grid(True)
        plt.show()