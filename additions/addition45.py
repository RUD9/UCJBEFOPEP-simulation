@staticmethod
def _save_config(value):
    # сохранение отчёта о начале процессов в JSON-файл
    with open('config_filename2.json', 'w') as config_file:
        json.dump(value, config_file)
