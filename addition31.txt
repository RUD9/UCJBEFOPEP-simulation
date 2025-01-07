
def calculate_photon_energy(self, wavelength):
    # Расчет энергии фотона по формуле E = hc/λ
    return self.constants['h'] * self.constants['c'] / wavelength

