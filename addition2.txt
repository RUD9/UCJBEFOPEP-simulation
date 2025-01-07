@staticmethod
def _create_cube(position=(0, 0, 0), color='cyan'):
    # Создание вершин куба с фиксированными координатами
    vertices = np.array([
        [1.6, 0.8, 0], [2.4, 0.8, 0], 
        [2.4, 1, 0], [1.6, 1, 0],
        [1.6, 0.8, 1], [2.4, 0.8, 1], 
        [2.4, 1, 1], [1.6, 1, 1]
    ])
    # Смещение вершин относительно заданной позиции
    vertices += position
    # Определение граней куба
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # нижняя
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # верхняя
        # ... другие грани
    ]
    # Создание 3D полигональной коллекции
    cube = Poly3DCollection(
        faces, 
        alpha=0.1, 
        facecolor='cyan', 
        edgecolor='blue'
    )
    return cube
