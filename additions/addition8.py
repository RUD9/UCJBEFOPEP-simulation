def _log_output_energy(self, output_photon_energy):
    # Сохранение энергии выходного фотона
    self.energy_history['output_photon'].append(output_photon_energy)
    print(f"Выходной фотон - Энергия: {output_photon_energy:.2e} Дж")
