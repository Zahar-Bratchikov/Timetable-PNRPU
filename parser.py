import os
import requests
from PyQt5.QtWidgets import QMessageBox


def download_excel_schedule(Group, Year, Number_of_group, Level_education, Season, time):
    # Сформировать URL на основе предоставленных параметров
    base_url = "https://pstu.ru/files/file/Abitur/timetable/"
    url = (f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}%20-"
           f"{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx")
    url2 = (f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}%20%20-"
            f"{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx")
    url3 = (f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20FPMM%20{Group}-"
            f"{Year}-{Number_of_group}{Level_education}%20%28{Season}%20%20{time}%20smeny%29.xlsx")
    # Отправить GET-запрос для загрузки файла
    response = requests.get(url)

    if response.status_code == 200:
        # Определить путь для сохранения файла
        filename = f"timetable.xlsx"
        filepath = os.path.join(os.getcwd(), filename)

        # Записать содержимое файла
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath
    else:
        response = requests.get(url2)
        if response.status_code == 200:
            # Определить путь для сохранения файла
            filename = f"timetable.xlsx"
            filepath = os.path.join(os.getcwd(), filename)

            # Записать содержимое файла
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
        else:
            response = requests.get(url3)
            if response.status_code == 200:
                # Определить путь для сохранения файла
                filename = f"timetable.xlsx"
                filepath = os.path.join(os.getcwd(), filename)

                # Записать содержимое файла
                with open(filepath, "wb") as f:
                    f.write(response.content)
                return filepath
            else:
                QMessageBox.critical(None, "Ошибка", "Не удалось загрузить файл.", QMessageBox.Ok)
                return None
