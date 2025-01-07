def __init__(self):
    # Создание фигуры с 3D проекцией
    self.fig = plt.figure(figsize=(8, 6))
    self.ax = self.fig.add_subplot(111, projection='3d')
    # Установка начальных условий
    self.setup_initial_conditions()

