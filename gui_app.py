import customtkinter as ctk

# Настраиваем внешний вид (Тёмная тема, как мы любим)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DroneApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.title("FPV Engineering Tool")
        self.geometry("400x300")

        # Добавляем текстовую надпись (Label)
        self.label = ctk.CTkLabel(self, text="Калькулятор полета", font=("Arial", 20))
        self.label.pack(pady=20) # pack размещает элемент по центру

        # Добавляем кнопку
        self.button = ctk.CTkButton(self, text="Рассчитать", command=self.button_callback)
        self.button.pack(pady=10)

    # Функция, которая сработает при нажатии на кнопку
    def button_callback(self):
        print("Кнопка нажата! Тут будет логика расчета.")

# Запуск программы
if __name__ == "__main__":
    app = DroneApp()
    app.mainloop() # Это бесконечный цикл, чтобы окно не закрывалось