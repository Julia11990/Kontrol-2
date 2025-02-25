import pandas as pd

# Загрузка Excel-файла
file = '2.xlsx'
df = pd.read_excel(file)

# Запрос у пользователя
try:
    num = int(input("Введите номер строки для вывода (начиная с 0): "))

    # Проверка на валидность номера строки
    if num < 0 or num >= len(df):
        print("Неверный номер строки.")
    else:
        print("Данные в строке", num, ":", df.iloc[num])
except ValueError:
    print("Пожалуйста, введите целое число.")