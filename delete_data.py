from edit_data import choice_num

def delete_note ():
  try:
    file = open('file.json', 'r')
    data = file.readlines()
    file.close()
    id_for_delete = choice_num()
    id_for_delete = id_for_delete - 1
    file = open('file.json', 'w')
    if id_for_delete < 0 or id_for_delete > len(data):
      print("Заметки с таким номером не существует")
    else:
      data.pop(id_for_delete)
      for i in range(len(data)):
        temp = data[i].split(';')
        temp[0] = str(i+1)
        data[i] = ';'.join(temp)
        file.write(data[i])
    file.close()
  except FileNotFoundError:
    file = open('file.json', 'w')
    file.close()
    print ("Файл с заметками не найден. Создан новый файл.")