import requests
import os


def download_excel_schedule(faculty, group, period):
    # Сформировать URL на основе предоставленных параметров
    base_url = "https://pstu.ru/files/file/Abitur/timetable/"
    url = f"{base_url}2023-2024%20Raspisanie%20zanyatijj%20{faculty}%20{group}%20({period}).xlsx"

    # Отправить GET-запрос для загрузки файла
    response = requests.get(url)

    if response.status_code == 200:
        # Определить путь для сохранения файла
        filename = f"{faculty}_{group}_{period}.xlsx"
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
faculty = "AKF"
group = "AD%20%20-21-1s"
period = "vesennijj%20%20posle%20smeny"

file_path = download_excel_schedule(faculty, group, period)
