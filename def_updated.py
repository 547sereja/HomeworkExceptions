documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}

def show_names():
  """Показывает имена, проверяет на KeyError
  """
  for document in documents:
    try:
      print(f"{document.get('name')}")
    except KeyError:
      print(f"no name")


def people():
  """
  Принимает номер документа и выводит имя
  """
  document_number = input("Введите номер документа-> ")
  for document in documents:
    if document.get('number') == document_number:
      print(document.get('name'))
      break
  else:
    print("Такого человека нет в базе")


def shelf():
  """
  Спрашивает номер документа и показывает номер полки
  """
  document_number = input("Введите номер документа-> ")
  for directory,data  in directories.items():
    for number in data:
      if number == document_number:
        print(f"Документ на {directory}-й полке")
        break
  else:
    print("Такой документ отсутствует")


def lists():
  """
  Выводит список всех документов
  """
  for document in documents:
    print(f"{document.get('type')},- {document.get('name')},- {document.get('number')}")


def add():
  """
  Спрашивает номер, тип, имя, номер полки и добаляет новый документ
  """
  number = input("Введите номер документа-> ")
  typ = input("Введите тип документа-> ")
  name = input("введите имя владельца-> ")
  directory = input("Введите номер полки где будем хранить ваш документ, у нас всего три полки-> ")
  new_dict = {'type': typ, 'number': number, 'name': name}
  documents.append(new_dict)
  for directory_1 in directories.keys():    
    if directory_1 == directory:
      directories[directory_1].append(str(number))
      break 
  else: 
    if directory_1 != directory:
      directories[directory] = [number]
      
  print(f"Добавлено на полку {directory}")


def inputs():
  while True:
    choice = input('_________________________________ \nВедите команду:\n\
    f - Попробовать новую функцию\
     p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
     l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n\
     s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
     a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.\n->')
    if choice == 'p':
      people()
      
    elif choice == 'l':
      lists() 
      
    elif choice == 's':
      shelf() 
      
    elif choice == 'a':
      add()
    
    elif choice == 'f':
      show_names()
      
    elif choice != 'a' and choice != 'l' and choice != 's' and choice != 'a' :
      break
inputs()  




