# Мы берем наш уже готовый класс (я упростил его для примера)
class FPVDrone:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print(f"🚀 {self.name} в воздухе!")

# --- НАСЛЕДОВАНИЕ ---
# LongRange "наследует" всё от FPVDrone
class LongRange(FPVDrone):
    def __init__(self, name, gps_version):
        # super() вызывает конструктор Родителя, чтобы записать имя
        super().__init__(name)
        self.gps = gps_version # Уникальная деталь дальнолета

    # Уникальный метод только для этого типа
    def return_to_home(self):
        print(f"🏠 {self.name} активировал RTH (GPS: {self.gps}). Возврат на точку взлета.")

# --- ТЕСТ ---
# Обычный дрон
base_quad = FPVDrone("Racer-1")
base_quad.fly()
base_quad.return_to_home()
# Дальнолет
lr_quad = LongRange("Discovery", "Ublox M10")
lr_quad.fly()             # Метод достался от "отца"
lr_quad.return_to_home()  # А это его личная фишка