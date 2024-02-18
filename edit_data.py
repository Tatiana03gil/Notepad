from datetime import date
from datetime import datetime

def edit_note ():
  try:
    file = open('file.json', 'r')
    data = file.readlines()
    file.close()
    id_for_change = choice_num ()
    if id_for_change < 0 or id_for_change > len(data):
      print("Заметки с таким номером не существует")
    else:
      id_for_change = id_for_change - 1
      file = open('file.json', 'w')
      temp = data[id_for_change].split("; ")
      title = input ("Введите заголовок: ").upper()
      note = input ("Введите заметку: ")
      current_date = date.today()
      current_time = datetime.now().time()
      temp[2] = title
      temp[3] = note
      change = (f' изм.: {current_date} {current_time.hour}:{current_time.minute}; \n')
      data[id_for_change] = "; ".join(temp)+"; " + change
      for i in range(len(data)):
        file.write(data[i])
      file.close()
  except FileNotFoundError:
    file = open('file.json', 'w')
    file.close()
    print ("Файл с заметками не найден. Создан новый файл.")
    
def choice_num ():
  choice = 0
  try:
    choice = int(input("Введите номер заметки: \n"))
  except ValueError:
    print("Ошибка! Введите номер заметки \n")
    choice = choice_num()
  return choice
