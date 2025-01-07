
def __init__(self, pump_wavelength=100e-9, crystal_type='BBO'):
        self.constants = {
            'h': 6.626e-34,
            'c': 3e8
        }
        self.pump_wavelength = pump_wavelength  # Длина волны насоса
        self.crystal_type = crystal_type        # Тип кристалла

