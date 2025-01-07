def __init__(self, wavelength_input=200e-9, crystal_length=10e-3):
        # Инициализация констант
        self.constants = {'h': 6.626e-34,  'c': 3e8 } # Скорость света;  Постоянная Планка
        # Параметры симуляции
        self.wavelength_input = wavelength_input  # Входная длина волны
        self.crystal_length = crystal_length      # Длина кристалла
        self.nonlinear_coefficient = 1e-12        # Нелинейный коэффициент
        
        # История энергий для каждого типа фотонов
        self.energy_history = {
            'photon1': [],      # Первый входной фотон
            'photon2': [],      # Второй входной фотон
            'output_photon': [] # Выходной фотон
        }

