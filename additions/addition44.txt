def _render_static_objects(self):
    # Список объектов для отрисовки
    objects = [
        # Каждый объект - кортеж с типом и параметрами
        ('cube', {'position': (0, 0, 0), 'color': 'cyan'}),
        ('cube', {'position': (0, -0.5, 0), 'color': 'magenta'}),
        ('cone', {
            'height': 0.5, 
            'radius': 0.25, 
            'position': (1.37, 3.5, 0), 
            'rotation_angle': -90
        }),
        # ... другие объекты
    ]
    # Создание и добавление каждого объекта на сцену
    for obj_type, params in objects:
        obj = self.create_geometric_primitive(obj_type, **params)
        # Обработка разных типов объектов (список или единичный объект)
        if isinstance(obj, list):
            for part in obj:
                self.ax.add_collection3d(part)
        else:
            self.ax.add_collection3d(obj)

