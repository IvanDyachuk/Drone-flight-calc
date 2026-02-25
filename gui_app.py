import customtkinter as ctk

# Настройки темы (попробуй "green" или "dark-blue", если надоест синий)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DroneApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Настройка окна
        self.title("FPV Flight Calculator v1.0")
        self.geometry("400x450")

        # 2. Заголовок
        self.header = ctk.CTkLabel(self, text="Расчет времени полета", font=("Roboto", 24))
        self.header.pack(pady=20)

        # 3. Поле ввода Емкости (mAh)
        self.entry_cap = ctk.CTkEntry(self, placeholder_text="Емкость батареи (mAh)")
        self.entry_cap.pack(pady=10)

        # 4. Поле ввода Тока (Amps)
        self.entry_amps = ctk.CTkEntry(self, placeholder_text="Средний ток (A)")
        self.entry_amps.pack(pady=10)

        # 5. Кнопка "Рассчитать"
        self.btn_calc = ctk.CTkButton(self, text="РАССЧИТАТЬ", command=self.calculate_flight)
        self.btn_calc.pack(pady=20)

        # 6. Поле для вывода результата (изначально пустое)
        self.lbl_result = ctk.CTkLabel(self, text="Ожидание данных...", font=("Roboto", 18))
        self.lbl_result.pack(pady=20)

    # --- ЛОГИКА (ДВИГАТЕЛЬ) ---
    def calculate_flight(self):
        try:
            # А. Забираем текст из полей (.get())
            cap_text = self.entry_cap.get()
            amps_text = self.entry_amps.get()

            # Б. Превращаем текст в числа (float)
            capacity = float(cap_text)
            amps = float(amps_text)

            # В. Считаем (твоя формула)
            # (mAh / 1000) -> Ah / Amps -> Часы * 60 -> Минуты
            flight_time = (capacity / 1000) / amps * 60

            # Г. Обновляем текст на экране (.configure())
            # И используем f-строку с форматированием .1f
            self.lbl_result.configure(text=f"⏱️ Время: {flight_time:.1f} мин", text_color="green")

        except ValueError:
            # Д. Если ввели буквы вместо цифр
            self.lbl_result.configure(text="❌ Ошибка! Введите числа.", text_color="red")
        except ZeroDivisionError:
            # Е. Если ток = 0
            self.lbl_result.configure(text="❌ Ток не может быть 0!", text_color="red")

if __name__ == "__main__":
    app = DroneApp()
    app.mainloop()