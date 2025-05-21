import csv
import json

# Студент 1: Титович Є.А.

csv_file = 'Laba13.csv'
json_file = 'Laba13.json'

students = [
    {'Name': 'Atos', 'Age': 20, 'Grade': 70},
    {'Name': 'Portos', 'Age': 22, 'Grade': 95},
    {'Name': 'Aramis', 'Age': 19, 'Grade': 86}
]

try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
        writer.writeheader()
        writer.writerows(students)
    print(f"[OK] CSV файл створено: {csv_file}")
except IOError as e:
    print(f"[Error] Помилка при створенні CSV файлу: {e}")

try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"[OK] Дані з CSV переписано у JSON файл: {json_file}")
except FileNotFoundError:
    print(f"[Error] CSV файл не знайдено: {csv_file}")
except json.JSONDecodeError as e:
    print(f"[Error] Помилка у форматі JSON: {e}")
except Exception as e:
    print(f"[Error] Інша помилка: {e}")

# Студент 2: Лисаченко П.А.

try: 

#Додаємо нового студента
    with open(json_file, mode='r+', encoding='utf-8') as file:
        students_json = json.load(file)
        students_json.append({'Name': 'Dartanyan', 'Age': 21, 'Grade': 100})
        file.seek(0)
        json.dump(students_json, file, indent=4)
        file.truncate()
    print(f"[OK] Dartanyan додано до JSON файлу")
except Exception as e:
    print(f"[Error] Помилка додавання до JSON: {e}")

#Копіюємо оновлених студентів з JSON до CSV
try:
    with open(json_file, mode='r', encoding='utf-8') as file:
        updated_students = json.load(file)

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
        writer.writeheader()
        writer.writerows(updated_students)
    print(f"[OK] Оновлені дані з JSON переписано у CSV файл")
except Exception as e:
    print(f"[Error] Помилка оновлення CSV: {e}")
