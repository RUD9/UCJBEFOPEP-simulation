def _trajectory_stage(self, frame):
    # Движение разделенных точек
    t = (frame - 100) / 50
    pos1 = self.pos11 + t * (self.entry_point - self.start_point + np.array([0, 0.64, 0]))
    pos2 = self.pos22 + t * (self.entry_point - self.start_point + np.array([0, 0.64, 0]))
     if frame == 153:
        self._save_config('1')
    if frame == 165:
        self._save_config('1')
    self.ax.scatter(*pos1, color='blue', s=100)
    self.ax.scatter(*pos2, color='green', s=100)


