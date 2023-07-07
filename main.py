import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import password

from PIL import Image
import customtkinter as CTk

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x420")  # Размеры окна
        self.title("Генератор паролей")  # Название сверху
        self.resizable(False, False)  # Запрет менять разрешения по вертикали и горизонтали

        self.logo = CTk.CTkImage(dark_image=Image.open("images.png"), size=(225, 225))  # Фон и изображение
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)  # Отображаем фон
        self.logo_label.grid(row=0, column=0)  # Разместили изображение в 0 строке и столбце

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")  # привязать к основному окну экрана, изменить цвет на прозрачный
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=300)  # поля вывода пароля, закрепить виджет на фрейме и длинная виджита
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = CTk.CTkButton(master=self.password_frame, text="Generate", width=100, command=self.set_password)  # Кнопка
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=self)  # опций сложности пароля, для слайдера
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        # Слайдер для длинны пароля, from_=0, to=100 диапазон, number_of_steps=100 всего шагов

        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")
        # columnspan=3 объединяем три строки

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)  # виджит выводит длинну пароля слайдера
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var, onvalue=digits, offvalue="")
        # ЧекБокс, variable=self.cb_digits_var ссылка на переменную, которая хранит
        # состояние флажка, onvalue передаёт значение птички, offvalue передаёт значение святой птички

        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var, onvalue=ascii_lowercase, offvalue="" )

        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var, onvalue=ascii_uppercase, offvalue="")

        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var, onvalue=punctuation, offvalue="")

        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.password_length_slider.set(12)  # По дефолту слайдер на 12
        self.password_length_entry.insert(0, 12)  # по дефолту значение генератора на 12
        self.appearance_mode_option_menu.set("system")  # по дефолту тема оформления "системная"

    def change_appearance_mode_event(self, new_appearance_mode):
        """Привязать к меню функцию смена темы"""
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        """Слайдер"""
        self.password_length_entry.delete(0, "end")  # удаляем с первого символа по последний
        self.password_length_entry.insert(0, int(value))  # привязываем число к ползунку

    def get_characters(self):
        """соединяем все строки в одну"""
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbol_var.get())

        return chars

    def set_password(self):
        """Вызываем функцию генераций пароля из файла password и передаём в неё данные"""
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
                                                          characters=self.get_characters()))

if __name__ == "__main__":
    app = App()
    app.mainloop()