from datetime import date
from datetime import datetime


def add_note():
  try:
    current_date = date.today()
    current_time = datetime.now().time()
    title = input("Введите заголовок: ").upper()
    note = input("Введите заметку: ")
    file = open('file.json', 'r')
    data = file.readlines()
    id = len(data) + 1
    file.close()
    file = open('file.json', 'a')
    file.write(
      f'{id}; {current_date} {current_time.hour}:{current_time.minute}; {title};'
      + f' {note}\n')
    file.close()
    print("Заметка сохранена.")
  except FileNotFoundError:
    file = open('file.json', 'w')
    file.close()
    print("Файл с заметками не найден. Создан новый файл.")
    
