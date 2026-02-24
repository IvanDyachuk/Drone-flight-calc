class LipoBattery:
    def __init__(self, cells, capacity_mah):
        self.cells =  cells        # Запиши входящие cells в self
        self.capacity = capacity_mah       # Запиши capacity в self
        self.voltage = self.cells * 3.7  # Считаем номинальное напряжение

    def info(self):
        # Выведи строку с информацией
        print(f"🔋 Батарея {self.cells}S ({self.voltage:.1f}V), Емкость: {self.capacity}mAh")

    def check_voltage(self, current_voltage_per_cell):
        # Если напряжение меньше 3.5 — кричим
        if current_voltage_per_cell < 3.5:
            print(f"⚠️ {current_voltage_per_cell}V -> ПОСАДКА! Батарея разряжена!")
        else:
            print(f"✅ {current_voltage_per_cell}V -> Полет нормальный.")

# --- ТЕСТ (Не меняй этот код) ---
my_battery = LipoBattery(6, 1300)  # Создаем 6S 1300mAh
my_battery.info()                  # Должно написать про 22.2V

my_battery.check_voltage(3.8)      # Должно быть ОК
my_battery.check_voltage(3.4)      # Должно быть ALARMзн