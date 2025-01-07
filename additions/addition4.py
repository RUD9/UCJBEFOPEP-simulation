def simulate_down_conversion(self):
    input_energy = self.constants['h'] * self.constants['c'] / self.pump_wavelength
    signal_wavelength = 2 * self.pump_wavelength
    idler_wavelength = 2 * self.pump_wavelength
    return {
        'input_energy': input_energy,
        'signal_energy': self.constants['h'] * self.constants['c'] / signal_wavelength,
        'idler_energy': self.constants['h'] * self.constants['c'] / idler_wavelength
    }
#Этот метод рассчитывает энергии входного, сигнального и холостого фотонов, используя формулу E = hc/λ.
