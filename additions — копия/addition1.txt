@staticmethod
def rotate_point(point, angle_deg):
    # Создание матрицы поворота вокруг оси X
    angle_rad = np.deg2rad(angle_deg)
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(angle_rad), -np.sin(angle_rad)],
        [0, np.sin(angle_rad), np.cos(angle_rad)]
    ])
    # Применение поворота к точке
    return np.dot(rotation_matrix, point)
Метод create_geometric_primitive():
@staticmethod
def create_geometric_primitive(primitive_type, **kwargs):
    # Словарь доступных примитивов
    primitives = {
        'cone': SceneRenderer._create_cone_3d,
        'cube': SceneRenderer._create_cube,
        'cylinder': SceneRenderer._create_horizontal_cylinder
    }
    # Вызов соответствующего метода создания примитива
    return primitives[primitive_type](**kwargs)
