
import time
import json
import threading
import numpy as np
import qutip as qt
import matplotlib.pyplot as plt

with open('config_filename2.json', 'w') as config_file:
    json.dump('1', config_file)

class PhotonSimulation:
    def __init__(self, wavelength_input=200e-9, crystal_length=10e-3):
        self.constants = {
            'h': 6.626e-34,  # Постоянная Планка
            'c': 3e8  # Скорость света
        }
        self.wavelength_input = wavelength_input
        self.crystal_length = crystal_length
        self.nonlinear_coefficient = 1e-12
        self.energy_history = {k: [] for k in ['photon1', 'photon2', 'output_photon']}

    def calculate_photon_energy(self, wavelength):
        return self.constants['h'] * self.constants['c'] / wavelength

    def simulate_interaction(self):
        print("Начало взаимодействия фотонов в кристалле PPKTP")

        photon1_energy = self.calculate_photon_energy(self.wavelength_input)
        photon2_energy = photon1_energy
        output_photon_energy = 2 * photon1_energy
        output_wavelength = (self.constants['h'] * self.constants['c']) / output_photon_energy

        self._wait_for_signal('config_filename2.json',
                              lambda: self._log_photon_energies(photon1_energy, photon2_energy),
                              interval=0.1)

        print("\nПроцесс генерации второй гармоники:")
        print(f"Входная длина волны: {self.wavelength_input * 1e9:.2f} нм")
        print(f"Выходная длина волны: {output_wavelength * 1e9:.2f} нм")

        self._wait_for_signal('config_filename2.json',
                              lambda: self._log_output_energy(output_photon_energy),
                              interval=0.1)

    def _log_photon_energies(self, photon1_energy, photon2_energy):
        self.energy_history['photon1'].append(photon1_energy)
        self.energy_history['photon2'].append(photon2_energy)
        print(f"Фотон 1 - Энергия: {photon1_energy:.2e} Дж")
        print(f"Фотон 2 - Энергия: {photon2_energy:.2e} Дж")

    def _log_output_energy(self, output_photon_energy):
        self.energy_history['output_photon'].append(output_photon_energy)
        print(f"Выходной фотон - Энергия: {output_photon_energy:.2e} Дж")

    def _wait_for_signal(self, filename, callback, interval=0.1):
        tqw = 0
        while True:
            tqw += 1
            time.sleep(interval)
            if tqw % 5 == 0:
                callback()

            with open(filename, 'r') as config_file:
                if json.load(config_file) == "1":
                    with open(filename, 'w') as config_file:
                        json.dump('0', config_file)
                    break

    def plot_energy_dynamics(self):
        plt.figure(figsize=(10, 6))
        for label, data in self.energy_history.items():
            plt.plot(data, label=f'{label} фотон')
        plt.title('Динамика энергии фотонов при генерации второй гармоники')
        plt.xlabel('Время')
        plt.ylabel('Энергия (Дж)')
        plt.legend()
        plt.show()


class SPDCSimulation:
    def __init__(self, pump_wavelength=100e-9, crystal_type='BBO'):
        self.constants = {
            'h': 6.626e-34,
            'c': 3e8
        }
        self.pump_wavelength = pump_wavelength
        self.crystal_type = crystal_type

    def simulate_spdc_type_ii(self):
        #def photon_generation_probability(wavelength, crystal_length, nonlinear_coeff):
            #base_prob = 1e-4
            #wavelength_factor = (1 / wavelength) ** 2
            #length_factor = np.exp(-crystal_length / 10e-3)
            #nonlinear_factor = nonlinear_coeff * 1e12
            #return base_prob * wavelength_factor * length_factor * nonlinear_factor

        horizontal = qt.basis(2, 0)
        vertical = qt.basis(2, 1)
        entangled_state = (horizontal * vertical.dag() - vertical * horizontal.dag()).unit()

        def generate_photon_pair():
            #gen_prob = photon_generation_probability(self.pump_wavelength, 5e-3, 2e-12)
            #print(gen_prob)
            #if np.random.random() < gen_prob:
            photon1 = np.random.choice([horizontal, vertical])
            photon2 = horizontal if photon1 == vertical else vertical
            return photon1, photon2
            #return None

        def get_vector(photon):
            return np.array([1, 0, 0]) if photon == horizontal else np.array([0, 0, 1])

        polarization_vectors = []
        pair = generate_photon_pair()
        if pair:
            photon1, photon2 = pair
            polarization_vectors.append({
                'photon1': get_vector(photon1),
                'photon2': get_vector(photon2)
            })

        return polarization_vectors, entangled_state

    def simulate_down_conversion(self):
        input_energy = self.constants['h'] * self.constants['c'] / self.pump_wavelength
        signal_wavelength = 2 * self.pump_wavelength
        idler_wavelength = 2 * self.pump_wavelength

        return {
            'input_energy': input_energy,
            'signal_energy': self.constants['h'] * self.constants['c'] / signal_wavelength,
            'idler_energy': self.constants['h'] * self.constants['c'] / idler_wavelength
        }


def process_simulation():
    while True:
        time.sleep(0.1)
        with open('config_filename2.json', 'r') as config_file:
            if json.load(config_file) == "1":
                with open('config_filename2.json', 'w') as config_file:
                    json.dump('0', config_file)
                break

    photon_sim = PhotonSimulation()
    photon_sim.simulate_interaction()

    spdc_sim = SPDCSimulation()
    down_conversion_result = spdc_sim.simulate_down_conversion()
    polarization_result, entangled_state = spdc_sim.simulate_spdc_type_ii()
    print('\nSPDCSimulation')

    while True:
        time.sleep(0.1)
        with open('config_filename2.json', 'r') as config_file:
            if json.load(config_file) == "1":
                with open('config_filename2.json', 'w') as config_file:
                    json.dump('0', config_file)
                break
    print_simulation_results(down_conversion_result, polarization_result)
    save_polarization_data(polarization_result)


def print_simulation_results(down_conversion_result, polarization_result):
    print("\nЭнергия входного фотона:", down_conversion_result['input_energy'], "Дж")
    print("Энергия сигнального фотона:", down_conversion_result['signal_energy'], "Дж")
    print("Энергия холостого фотона:", down_conversion_result['idler_energy'], "Дж")

    for i, pair in enumerate(polarization_result, 1):
        print(f"Пара {i}:")
        print(f"Фотон 1: {pair['photon1']}")
        print(f"Фотон 2: {pair['photon2']}\n")


def save_polarization_data(polarization_result):
    p1, p2 = str(polarization_result[0]['photon1']), str(polarization_result[0]['photon2'])
    with open('config_filename4.json', 'w') as config_file:
        json.dump('1', config_file)
    with open('config_filename5.json', 'w') as config_file:
        json.dump(''.join(p1), config_file)
    with open('config_filename11.json', 'w') as config_file:
        json.dump(''.join(p2), config_file)


def main():
    simulation_thread = threading.Thread(target=process_simulation)
    simulation_thread.start()
    simulation_thread.join()


if __name__ == "__main__":
    while True:
        main()

