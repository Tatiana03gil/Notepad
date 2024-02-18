def open_note ():
  try:
    file = open('file.json', 'r')
    print(file.read())
    file.close()
  except FileNotFoundError:
    file = open('file.json', 'w')
    file.close()
  print("Файл c заметками не найден. Создан новый файл.")

def open_note_by_date ():
  try:
    file = open('file.json', 'r')
    date = input("Введите дату в формате yyyy-mm-dd: ")
    count = 0
    print()
    for line in file:
      if date in line:
        print(line)
        count += 1
    if count == 0: 
      print("Заметок с такой датой не найдено")
    file.close()
  except FileNotFoundError:
    file = open('file.json', 'w')
    file.close()
    print("Файл c заметками не найден. Создан новый файл.")