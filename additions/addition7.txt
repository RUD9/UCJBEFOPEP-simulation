def _log_photon_energies(self, photon1_energy, photon2_energy):
    # Сохранение энергий во внутреннюю историю
    self.energy_history['photon1'].append(photon1_energy)
    self.energy_history['photon2'].append(photon2_energy)
    
    # Вывод энергий
    print(f"Фотон 1 - Энергия: {photon1_energy:.2e} Дж")
    print(f"Фотон 2 - Энергия: {photon2_energy:.2e} Дж")

