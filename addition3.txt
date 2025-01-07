@staticmethod
def _create_horizontal_cylinder(
    position=(1.37, 2, 0), 
    length=1, 
    radius=0.15, 
    color='grey'
):
    # Создание параметрических точек для цилиндра
    theta = np.linspace(0, 2 * np.pi, 100)
    # Центральная ось цилиндра
    x = np.ones(2) * position[0]
    y = np.linspace(position[1], position[1] + length, 2)
    z = np.ones(2) * position[2]
    # Создание сетки координат
    theta_grid, y_grid = np.meshgrid(theta, y)
    # Вычисление координат поверхности цилиндра
    x_cylinder = radius * np.cos(theta_grid) + position[0]
    z_cylinder = radius * np.sin(theta_grid) + position[2]
    # Создание списка поверхностей цилиндра
    cylinder = []
    # Добавление торцов цилиндра
    cylinder.append(Poly3DCollection([
        list(zip(x_cylinder[0], y_grid[0], z_cylinder[0]))
    ], alpha=0.1, facecolor=color, edgecolor='green'))
    # Добавление боковых поверхностей
    for i in range(len(theta) - 1):
        side_face = [
            (x_cylinder[0, i], y_grid[0, i], z_cylinder[0, i]),
            (x_cylinder[0, i + 1], y_grid[0, i + 1], z_cylinder[0, i + 1]),
            (x_cylinder[1, i + 1], y_grid[1, i + 1], z_cylinder[1, i + 1]),
            (x_cylinder[1, i], y_grid[1, i], z_cylinder[1, i])
        ]
        cylinder.append(Poly3DCollection(
            [side_face], 
            alpha=0.1, 
            facecolor=color, 
            edgecolor='green'
        ))
    return cylinder
