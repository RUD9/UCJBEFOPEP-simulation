#Метод _create_cone_3d() - создание 3D конуса:
@staticmethod
def _create_cone_3d(height=5, radius=3, position=(0,0,0), color='cyan', 
                    alpha=0.5, rotation_angle=90):
    # Генерация точек основания конуса
    theta = np.linspace(0, 2 * np.pi, 50)
    base_x = radius * np.cos(theta)
    base_y = radius * np.sin(theta)
    base_z = np.zeros_like(base_x)
    # Создание вершины конуса
    apex_x, apex_y, apex_z = 0, 0, height
    # Поворот и позиционирование конуса
    # ... (сложные преобразования координат)
    # Создание многогранной коллекции для отрисовки
    cone_collection = Poly3DCollection(
        all_faces,
        facecolors=color,
        edgecolors='black',
        alpha=alpha
    )
    return cone_collection
