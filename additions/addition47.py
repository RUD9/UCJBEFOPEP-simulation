def _animate_point(self, frame):
    # Определение этапов анимации с границами кадров
    frame_stages = [
        (50, self._entry_stage),     # 1-й этап до 50 кадра
        (100, self._split_stage),    # 2-й этап до 100 кадра
        (170, self._trajectory_stage) # 3-й этап до 170 кадра
    ]
    # Выбор и выполнение текущего этапа
    for max_frame, stage_method in frame_stages:
        if frame < max_frame:
            stage_method(frame)
            break
