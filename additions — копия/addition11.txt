#Сохранение данных поляризации:
def save_polarization_data(polarization_result):
    p1, p2 = str(polarization_result[0]['photon1']), str(polarization_result[0]['photon2'])
    with open('config_filename4.json', 'w') as config_file:
        json.dump('1', config_file)
    with open('config_filename5.json', 'w') as config_file:
        json.dump(''.join(p1), config_file)
    with open('config_filename11.json', 'w') as config_file:
        json.dump(''.join(p2), config_file)
#Этот метод сохраняет данные о поляризации фотонов в JSON файлы для дальнейшего использования или анализа.
