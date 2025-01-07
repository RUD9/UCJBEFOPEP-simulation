import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import json


class SceneRenderer:
    def __init__(self):
        self.fig = plt.figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.setup_initial_conditions()

    def setup_initial_conditions(self):
        self.start_point = np.array([2, 0, 0])
        self.entry_point = np.array([2, 0.9, 0])
        self.split_point = np.array([2, 0.9, 0])
        self.angle1 = np.radians(50)
        self.angle2 = np.radians(130)

    @staticmethod
    def rotate_point(point, angle_deg):
        angle_rad = np.deg2rad(angle_deg)
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad)],
            [0, np.sin(angle_rad), np.cos(angle_rad)]
        ])
        return np.dot(rotation_matrix, point)

    @staticmethod
    def create_geometric_primitive(primitive_type, **kwargs):
        primitives = {
            'cone': SceneRenderer._create_cone_3d,
            'cube': SceneRenderer._create_cube,
            'cylinder': SceneRenderer._create_horizontal_cylinder
        }
        return primitives[primitive_type](**kwargs)

    @staticmethod
    def _create_cone_3d(height=5, radius=3, position=(0, 0, 0), color='cyan', alpha=0.5, rotation_angle=90):
        """
        Создание геометрии конуса для add_collection3d с возможностью поворота

        Параметры:
        - height: высота конуса
        - radius: радиус основания
        - position: центр основания конуса (x,y,z)
        - color: цвет конуса
        - alpha: прозрачность
        - rotation_angle: угол поворота в градусах

        Возвращает коллекцию многогранников
        """
        x0, y0, z0 = position

        # Создаем точки основания
        theta = np.linspace(0, 2 * np.pi, 50)
        base_x = radius * np.cos(theta)
        base_y = radius * np.sin(theta)
        base_z = np.zeros_like(base_x)

        # Верхушка конуса
        apex_x = 0
        apex_y = 0
        apex_z = height

        # Поворачиваем точки
        rotated_base = [
            SceneRenderer.rotate_point([x, y, z], rotation_angle)
            for x, y, z in zip(base_x, base_y, base_z)
        ]
        rotated_apex = SceneRenderer.rotate_point([apex_x, apex_y, apex_z], rotation_angle)

        # Разделяем повернутые координаты
        base_x_rot = [p[0] for p in rotated_base]
        base_y_rot = [p[1] for p in rotated_base]
        base_z_rot = [p[2] for p in rotated_base]

        # Смещаем координаты
        base_x_final = [x + x0 for x in base_x_rot]
        base_y_final = [y + y0 for y in base_y_rot]
        base_z_final = [z + z0 for z in base_z_rot]

        apex_x_final = rotated_apex[0] + x0
        apex_y_final = rotated_apex[1] + y0
        apex_z_final = rotated_apex[2] + z0

        # Формируем грани конуса
        faces = []

        # Основание конуса
        base_points = [list(zip(base_x_final, base_y_final, base_z_final))]

        # Боковые грани
        for i in range(len(theta)):
            face = [
                (base_x_final[i], base_y_final[i], base_z_final[i]),
                (
                    base_x_final[(i + 1) % len(theta)], base_y_final[(i + 1) % len(theta)],
                    base_z_final[(i + 1) % len(theta)]),
                (apex_x_final, apex_y_final, apex_z_final)
            ]
            faces.append(face)

        # Объединяем основание и боковые грани
        all_faces = base_points + faces

        # Создаем коллекцию многогранников
        cone_collection = Poly3DCollection(
            all_faces,
            facecolors=color,
            edgecolors='black',
            alpha=alpha
        )

        return cone_collection

    # (Код создания конуса остается прежним)
    # ...

    @staticmethod
    def _create_cube(position=(0, 0, 0), color='cyan'):
        # Вершины куба
        vertices = np.array([
            [1.6, 0.8, 0], [2.4, 0.8, 0], [2.4, 1, 0], [1.6, 1, 0],
            [1.6, 0.8, 1], [2.4, 0.8, 1], [2.4, 1, 1], [1.6, 1, 1]
        ])
        vertices += position

        # Грани куба
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],  # нижняя
            [vertices[4], vertices[5], vertices[6], vertices[7]],  # верхняя
            [vertices[0], vertices[1], vertices[5], vertices[4]],  # передняя
            [vertices[2], vertices[3], vertices[7], vertices[6]],  # задняя
            [vertices[1], vertices[2], vertices[6], vertices[5]],  # правая
            [vertices[0], vertices[3], vertices[7], vertices[4]]  # левая
        ]

        # Создание 3D полигонов
        cube = Poly3DCollection(faces, alpha=0.1, facecolor='cyan', edgecolor='blue')
        return cube

    # (Код создания куба остается прежним)
    # ...

    @staticmethod
    def _create_horizontal_cylinder(position=(1.37, 2, 0), length=1, radius=0.15, color='grey'):
        # Создание торцов цилиндра
        theta = np.linspace(0, 2 * np.pi, 100)

        # Центральная ось цилиндра
        x = np.ones(2) * position[0]
        y = np.linspace(position[1], position[1] + length, 2)
        z = np.ones(2) * position[2]

        # Круговые сечения
        theta_grid, y_grid = np.meshgrid(theta, y)

        x_cylinder = radius * np.cos(theta_grid) + position[0]
        z_cylinder = radius * np.sin(theta_grid) + position[2]

        # Боковая поверхность цилиндра
        cylinder = []

        # Торцы цилиндра
        cylinder.append(Poly3DCollection([list(zip(x_cylinder[0], y_grid[0], z_cylinder[0]))],
                                         alpha=0.1, facecolor=color, edgecolor='green'))
        cylinder.append(Poly3DCollection([list(zip(x_cylinder[1], y_grid[1], z_cylinder[1]))],
                                         alpha=0.1, facecolor=color, edgecolor='green'))

        # Боковая поверхность
        for i in range(len(theta) - 1):
            side_face = [
                (x_cylinder[0, i], y_grid[0, i], z_cylinder[0, i]),
                (x_cylinder[0, i + 1], y_grid[0, i + 1], z_cylinder[0, i + 1]),
                (x_cylinder[1, i + 1], y_grid[1, i + 1], z_cylinder[1, i + 1]),
                (x_cylinder[1, i], y_grid[1, i], z_cylinder[1, i])
            ]
            cylinder.append(Poly3DCollection([side_face], alpha=0.1, facecolor=color, edgecolor='green'))

        return cylinder

    # к
    # ...

    def update(self, frame):
        self.ax.clear()
        self._render_static_objects()
        self._animate_point(frame)
        self._set_scene_limits()

    def _render_static_objects(self):
        objects = [
            ('cube', {'position': (0, 0, 0), 'color': 'cyan'}),
            ('cube', {'position': (0, -0.5, 0), 'color': 'magenta'}),
            ('cone', {'height': 0.5, 'radius': 0.25, 'position': (1.37, 3.5, 0), 'rotation_angle': -90}),
            ('cone', {'height': 0.5, 'radius': 0.25, 'position': (2.63, 3.5, 0), 'rotation_angle': -90}),
            ('cylinder', {'position': (1.37, 2, 0)}),
            ('cylinder', {'position': (2.63, 2, 0)}),
            ('cylinder', {'position': (1.37, 3.25, 0), 'length': 0.05, 'radius': 0.25, 'color': 'cyan'}),
            ('cylinder', {'position': (2.63, 3.25, 0), 'length': 0.05, 'radius': 0.25, 'color': 'cyan'})
        ]

        for obj_type, params in objects:
            obj = self.create_geometric_primitive(obj_type, **params)
            if isinstance(obj, list):
                for part in obj:
                    self.ax.add_collection3d(part)
            else:
                self.ax.add_collection3d(obj)

    def _animate_point(self, frame):
        frame_stages = [
            (50, self._entry_stage),
            (100, self._split_stage),
            (170, self._trajectory_stage)
        ]

        for max_frame, stage_method in frame_stages:
            if frame < max_frame:
                stage_method(frame)
                break

    def _entry_stage(self, frame):
        if frame == 24:
            self._save_config('1')
        t = frame / 50
        pos = self.start_point + t * (self.entry_point - self.start_point)
        self.ax.scatter(*pos, color='red', s=100)

    def _split_stage(self, frame):
        if frame == 51:
            self._save_config('1')
        t = (frame + 50 - 100) / 50
        self.pos11 = self.split_point + t * np.array([np.cos(self.angle1), np.sin(self.angle1), 0])
        self.pos22 = self.split_point + t * np.array([np.cos(self.angle2), np.sin(self.angle2), 0])
        self.ax.scatter(*self.pos11, color='blue', s=100)
        self.ax.scatter(*self.pos22, color='green', s=100)

    def _trajectory_stage(self, frame):
        t = (frame - 100) / 50
        pos1 = self.pos11 + t * (self.entry_point - self.start_point + np.array([0, 0.64, 0]))
        pos2 = self.pos22 + t * (self.entry_point - self.start_point + np.array([0, 0.64, 0]))

        if frame == 153:
            self._save_config('1')
        if frame == 165:
            self._save_config('1')

        self.ax.scatter(*pos1, color='blue', s=100)
        self.ax.scatter(*pos2, color='green', s=100)

    def _set_scene_limits(self):
        self.ax.set_xlim(0, 4)
        self.ax.set_ylim(0, 4)
        self.ax.set_zlim(0, 4)
        self.ax.set_title('Анимация точки в кубе')

    @staticmethod
    def _save_config(value):
        with open('config_filename2.json', 'w') as config_file:
            json.dump(value, config_file)

    def run_animation(self):
        anim = FuncAnimation(self.fig, self.update, frames=170, interval=20)
        plt.show()


if __name__ == "__main__":
    scene = SceneRenderer()
    scene.run_animation()

