documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def prompt_doc_number():
    return input('Введите номер документа:\n')


def prompt_shelf_number():
    return input('Введите номер полки:\n')


def get_proprietor():
    """Searches for a document in the list 'documents' by the prompting user for the document number.
    Returns the owner of the document if the document is found,
    else - a fault message.
    """
    number = prompt_doc_number()
    for doc in documents:
        if doc.get('number') == number:
            return f"Владелец документа: {doc.get('name', 'не найден')}"
    return 'Документ не найден в базе'


def get_shelf(number):
    for shelf, docs in directories.items():
        if number in docs:
            return f'полка хранения: {shelf}'
    return 'Документ не найден в базе'


def list_docs():
    print('Текущий список документов: ')
    [print(
        f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, {get_shelf(doc['number'])}"
    ) for doc in documents]


def list_shelves():
    print(f"Текущий перечень полок: {', '.join(directories.keys())}.")


def add_shelf():
    shelf = prompt_shelf_number()
    if shelf_exists(shelf):
        print('Такая полка уже существует.', end=' ')
    else:
        directories.setdefault(shelf, [])
        print('Полка добавлена.', end=' ')
    list_shelves()


def shelf_exists(shelf):
    if shelf in directories:
        return True
    return False


def shelf_is_empty(shelf):
    if len(directories.get(shelf)) == 0:
        return True
    return False


def del_shelf():
    shelf = prompt_shelf_number()
    if shelf_exists(shelf):
        if shelf_is_empty(shelf):
            del directories[shelf]
            print('Полка удалена.', end=' ')
        else:
            print('На полке есть документы, удалите их перед удалением полки.', end=' ')
    else:
        print('Такой полки не существует.', end=' ')
    list_shelves()


def add_doc():
    number = prompt_doc_number()
    doc_type = input('Введите тип документа:\n')
    name = input('Введите владельца документа:\n')
    shelf = prompt_shelf_number()

    if shelf_exists(shelf):
        documents.append(dict((('type', doc_type), ('number', number), ('name', name))))
        directories.get(shelf).append(number)
        print('Документ добавлен.', end=' ')
    else:
        print('Такой полки не существует. Добавьте полку командой ads.')

    list_docs()


def doc_exists(number):
    for shelf, docs_list in directories.items():
        if number in docs_list:
            return True, shelf
    return (False, '')


def del_doc():
    number = prompt_doc_number()
    checking_doc, shelf = doc_exists(number)

    if checking_doc:
        directories.get(shelf).remove(number)
        for doc in documents:
            if doc.get('number') == number:
                documents.remove(doc)
                print('Документ удален.', end=' ')
    else:
        print('Документ не найден в базе.', end=' ')

    list_docs()


def move_doc():
    number = prompt_doc_number()
    shelf_to = prompt_shelf_number()

    if shelf_exists(shelf_to):
        checking_doc, shelf_from = doc_exists(number)

        if checking_doc:
            directories.get(shelf_to).append(number)
            directories.get(shelf_from).remove(number)
            print('Документ перемещен.', end=' ')
            list_docs()
        else:
            print('Документ не найден в базе.', end=' ')
            list_docs()
    else:
        print('Такой полки не существует.', end=' ')
        list_shelves()


def main():
    qwery = ''
    while qwery != 'q':
        qwery = input('p - узнать владельца документа,\n'
                      's - узнать на какой полке хранится документ,\n'
                      'l - полная информация по всем документам,\n'
                      'ads - добавить новую полку,\n'
                      'ds - удалить существующую полку из данных,\n'
                      'ad - добавить новый документ,\n'
                      'd - удалить документ,\n'
                      'm - переместить документ с полки на полку,\n'
                      'q - ВЫХОД из программы\n'
                      'Введите команду: ').strip()
        if qwery == 'p':
            print(get_proprietor())
        elif qwery == 's':
            number = prompt_doc_number()
            print(get_shelf(number))
        elif qwery == 'l':
            list_docs()
        elif qwery == 'ads':
            add_shelf()
        elif qwery == 'ds':
            del_shelf()
        elif qwery == 'ad':
            add_doc()
        elif qwery == 'd':
            del_doc()
        elif qwery == 'm':
            move_doc()
        else:
            print('Ошибка ввода')
        print('--------------------------------------------------')


main()
