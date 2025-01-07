def update(self, frame):
    self.ax.clear()     # Очистка текущего кадра
    self._render_static_objects()    # Отрисовка статических объектов
    self._animate_point(frame)    # Анимация точек
    self._set_scene_limits()    # Установка границ сцены
