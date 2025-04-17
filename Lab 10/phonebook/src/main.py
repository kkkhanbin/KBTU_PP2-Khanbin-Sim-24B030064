import csv

from db import insert, update, get, delete

quit_key = 'q'

MAIN_MENU_MSG = f'''
1 - Insert
2 - Update
3 - Get
4 - Delete

{quit_key} - Quit
'''

INSERT_MSG = '''
1 - Get data from csv file
2 - Input data manually
'''

CSV_MSG = '''
Input csv-file path: 
'''

GET_MSG = '''
1 - By ID
2 - By name
'''


def main():
    action = input(MAIN_MENU_MSG)

    while action != quit_key:
        if action == '1':
            action = input(INSERT_MSG)

            if action == '1':
                path = input(CSV_MSG)

                with open(path, 'r') as file:
                    persons = list(csv.reader(file, delimiter=';'))

                insert(persons)

            elif action == '2':
                name = input('Name: ')
                surname = input('Surname: ')
                phone_number = input('Phone number: ')

                insert([[name, surname, phone_number]])

        elif action == '2':
            person_id = input('ID: ')
            name = input('New name: ')
            surname = input('New surname: ')
            phone_number = input('New phone number: ')

            update(person_id, [name, surname, phone_number])

        elif action == '3':
            action = input(GET_MSG)

            if action == '1':
                person_id = input('ID: ')

                found = get({'id': person_id})

                if not found:
                    print('Nothing has been found.')
                else:
                    print(''.join(map(lambda el: str(el.ljust(30)), ['name', 'surname', 'phone_number', 'id'])))
                    print('\n'.join(map(lambda row: ''.join(map(lambda el: str(el).ljust(30), row)), found)))

            elif action == '2':
                name = input('Name: ')

                found = get({'name': name})

                if not found:
                    print('Nothing has been found.')
                else:
                    print(''.join(map(lambda el: str(el.ljust(30)), ['name', 'surname', 'phone_number', 'id'])))
                    print('\n'.join(map(lambda row: ''.join(map(lambda el: str(el).ljust(30), row)), found)))

        elif action == '4':
            person_id = input('ID: ')

            delete(person_id)

        action = input(MAIN_MENU_MSG)


if __name__ == "__main__":
    main()
    print("Bye.")