import requests
import json
from tkinter import *
from tkinter import  messagebox as mb
from tkinter import  ttk


def update_b_1_label(event):
    code = b_1_combobox.get()
    name = cur[code]
    b_1_label.config(text = name)


def update_b_2_label(event):
    code = b_2_combobox.get()
    name = cur[code]
    b_2_label.config(text = name)


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text = name)


def exchange():
    t_code = t_combobox.get()
    b_1_code = b_1_combobox.get()
    b_2_code = b_2_combobox.get()

    if t_code and b_1_code and b_2_code:
        try:
            response_1 = requests.get(f'https://open.er-api.com/v6/latest/{b_1_code}')
            response_1.raise_for_status()
            data_1 = response_1.json()

            response_2 = requests.get(f'https://open.er-api.com/v6/latest/{b_2_code}')
            response_2.raise_for_status()
            data_2 = response_2.json()

            if t_code in data_1['rates']:
                exchange_rate_1 = data_1['rates'][t_code]
                t_name = cur[t_code]
                b_1_name = cur[b_1_code]

                if t_code in data_2['rates']:
                    exchange_rate_2 = data_2['rates'][t_code]
#                    t_name = cur[t_code]
                    b_2_name = cur[b_2_code]

                    mb.showinfo('Курс обмена',
                                f'Курс:\n{exchange_rate_1:.2f} {t_name} за 1 {b_1_name},\n{exchange_rate_2:.2f} {t_name} за 1 {b_2_name}.')
            else:
                mb.showerror('Ошибка!', f'Валюта {t_code} не найдена.')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты.')


cur = {
    'RUB': 'Российский рубль',
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекистанский сум',
    'CHF': 'Швейцарский франк',
    'UAH': 'Украинская гривна'
}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x440')

Label(text = 'Базовая валюта 1').pack(padx = 10, pady = 10)
b_1_combobox = ttk.Combobox(values = list(cur.keys()))
b_1_combobox.pack(padx = 10, pady = 10)
b_1_combobox.bind('<<ComboboxSelected>>', update_b_1_label)

b_1_label = ttk.Label()
b_1_label.pack(padx = 10, pady = 10)

Label(text = 'Базовая валюта 2').pack(padx = 10, pady = 10)
b_2_combobox = ttk.Combobox(values = list(cur.keys()))
b_2_combobox.pack(padx = 10, pady = 10)
b_2_combobox.bind('<<ComboboxSelected>>', update_b_2_label)

b_2_label = ttk.Label()
b_2_label.pack(padx = 10, pady = 10)

Label(text = 'Целевая валюта').pack(padx = 10, pady = 10)
t_combobox = ttk.Combobox(values = list(cur.keys()))
t_combobox.pack(padx = 10, pady = 10)
t_combobox.bind('<<ComboboxSelected>>', update_t_label)

t_label = ttk.Label()
t_label.pack(padx = 10, pady = 10)

Button(text = 'Получить курс обмена', command = exchange).pack(padx = 10, pady = 10)

window.mainloop()
