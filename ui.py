from add_data import add_note
from datetime import date, datetime
from delete_data import delete_note
from open_data import open_note, open_note_by_date
from edit_data import edit_note


def start_menu ():
    command = None
    while command != 6:
      print('Доброго времени суток! \n')
      command = command_num()        
      command = check_number(command)
      if command == 1:
          add_note()
      if command == 2:
          open_note()
      if command == 3:
          open_note_by_date()
      if command == 4:
          delete_note()
      if command == 5:
          edit_note()
      if command == 6:
          break
    print ("Спасибо за работу!\n"
           "Приходите к нам ещё!")

def check_number (n):
    while n < 1 or n > 6:
      print('Ошибка! Такой комманды нет! \n'
            'Выберите комманду от 1 до 6 \n')
      n = command_num()
    return n

def command_num ():
  command = None
  try:
    command = int(input(
    'Выберите комманду для работы с заметками \n'
    '1. Добавить заметку \n'
    '2. Открыть заметки (все) \n'
    '3. Открыть заметки по дате \n'
    '4. Удалить заметку \n'
    '5. Редактировать заметку \n'
    '6. Выход \n'
    ))
  except ValueError:
    print('Ошибка! Такой комманды нет! \n'
          'Выберите комманду от 1 до 6 \n')
    command = command_num()
  return command