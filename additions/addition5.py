#Вывод результатов симуляции:
def print_simulation_results(down_conversion_result, polarization_result):
    print("\nЭнергия входного фотона:", down_conversion_result['input_energy'], "Дж")
    print("Энергия сигнального фотона:", down_conversion_result['signal_energy'], "Дж")
    print("Энергия холостого фотона:", down_conversion_result['idler_energy'], " Дж")
    for i, pair in enumerate(polarization_result, 1):
        print(f"Пара {i}:")
        print(f"Фотон 1: {pair['photon1']}")
        print(f"Фотон 2: {pair['photon2']}\n")
#Этот метод выводит на экран энергии входного, сигнального и холостого фотонов, а также информацию о спаренных фотонах.
