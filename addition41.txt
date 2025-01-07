def _split_stage(self, frame):
     if frame == 51:
         self._save_config('1')
    # Разделение точки на две траектории
    t = (frame + 50 - 100) / 50
    self.pos11 = self.split_point + t * np.array([np.cos(self.angle1), np.sin(self.angle1), 0])
    self.pos22 = self.split_point + t * np.array([np.cos(self.angle2), np.sin(self.angle2), 0])
    self.ax.scatter(*self.pos11, color='blue', s=100)
    self.ax.scatter(*self.pos22, color='green', s=100)
