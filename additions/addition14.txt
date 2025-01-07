#Метод _set_scene_limits():
def _set_scene_limits(self):
    # Установка границ 3D сцены
    self.ax.set_xlim(0, 4)
    self.ax.set_ylim(0, 4)
    self.ax.set_zlim(0, 4)
    self.ax.set_title('Анимация')

