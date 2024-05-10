import requests
import os


def download_excel_schedule(Faculty, Group, Year, Number_of_group, Season, time):
    # Сформировать URL на основе предоставленных параметров
    base_url = "https://pstu.ru/files/file/Abitur/timetable/"
    url = f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20{Faculty}%20{Group}%20-{Year}-{Number_of_group}%20%28{Season}%20%20{time}%20smeny%29.xlsx"

    # Отправить GET-запрос для загрузки файла
    response = requests.get(url)

    if response.status_code == 200:
        # Определить путь для сохранения файла
        filename = f"{Faculty}_{Group}-{Year}-{Number_of_group}.xlsx"
        filepath = os.path.join(os.getcwd(), filename)

        # Записать содержимое файла
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Файл {filename} успешно загружен.")
        return filepath
    else:
        print("Не удалось загрузить файл.")
        return None


# Пример использования функции

#https://pstu.ru/files/file/Abitur/timetable/2023-2024%20Raspisanie%20zanyatijj%20{Faculty}%20{Group}%20-{Year}-{Number_of_group }%20%28{Season}%20%20{time}%20smeny%29.xlsx
Faculty = "FPMM"
Group = "IST"
Year = "21"
Number_of_group = "2b"
Season = "osennijj"
time = "posle"

file_path = download_excel_schedule(Faculty, Group, Year, Number_of_group, Season, time)
if file_path:
    # Теперь можно прочитать файл Excel и обработать его с помощью pandas или openpyxl
    # Например, можно использовать pandas:
    """import pandas as pd

    df = pd.read_excel(file_path)
    print(df.head())  # Вывести первые несколько строк расписания"""
