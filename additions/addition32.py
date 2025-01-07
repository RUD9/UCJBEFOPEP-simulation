def simulate_interaction(self):
    # Расчет энергий фотонов
    photon1_energy = self.calculate_photon_energy(self.wavelength_input)
    photon2_energy = photon1_energy
    output_photon_energy = 2 * photon1_energy
    # Расчет выходной длины волны
    output_wavelength = (self.constants['h'] * self.constants['c']) / output_photon_energy
    # Ожидание сигнала и логирование энергий
    self._wait_for_signal('config_filename2.json',
                          lambda: self._log_photon_energies(photon1_energy, photon2_energy),
                          interval=0.1)
    # Вывод информации о процессе
    print("\nПроцесс генерации второй гармоники:")
    print(f"Входная длина волны: {self.wavelength_input * 1e9:.2f} нм")
    print(f"Выходная длина волны: {output_wavelength * 1e9:.2f} нм")
    # Ожидание сигнала и логирование выходной энергии
    self._wait_for_signal('config_filename2.json',
                          lambda: self._log_output_energy(output_photon_energy),
                          interval=0.1)

