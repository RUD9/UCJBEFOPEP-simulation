def setup_initial_conditions(self):
    # Определение ключевых точек траектории
    self.start_point = np.array([2, 0, 0])     # Начальная точка
    self.entry_point = np.array([2, 0.9, 0])   # Точка входа
    self.split_point = np.array([2, 0.9, 0])   # Точка разделения
    self.angle1 = np.radians(50)   # Первый угол движения
    self.angle2 = np.radians(130)  # Второй угол движения

