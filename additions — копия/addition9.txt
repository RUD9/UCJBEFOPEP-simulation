#Метод ожидания сигнала:
def _wait_for_signal(self, filename, callback, interval=0.1):
    tqw = 0
    while True:
        tqw += 1
        time.sleep(interval) 
        # Периодический вызов колбэка
        if tqw % 5 == 0:
            callback()
        # Проверка файла конфигурации
        with open(filename, 'r') as config_file:
            if json.load(config_file) == "1":
                # Сброс файла
                with open(filename, 'w') as config_file:
                    json.dump('0', config_file)
                break
#Реализует механизм межпроцессного взаимодействия через файл.


