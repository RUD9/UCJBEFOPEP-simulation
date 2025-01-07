def _entry_stage(self, frame):
     if frame == 24:
         self._save_config('1')
    # Движение точки от начальной до точки входа
    t = frame / 50
    pos = self.start_point + t * (self.entry_point - self.start_point)
    self.ax.scatter(*pos, color='red', s=100)
