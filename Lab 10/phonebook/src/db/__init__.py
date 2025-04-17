from .config import load_config
from .db import connect

connection = connect(load_config('db/database.ini'))


def insert(persons):
    sql = '''
INSERT INTO phonebook_schema.persons(name, surname, phone_number)
VALUES(%s, %s, %s) RETURNING *;
'''

    with connection.cursor() as cur:
        cur.executemany(sql, persons)
        connection.commit()

    print('Created.')
    return True


def update(person_id, person):
    sql = '''
UPDATE phonebook_schema.persons
SET name = %s, surname = %s, phone_number = %s
WHERE id = %s
'''

    with connection.cursor() as cur:
        cur.execute(sql, (*person, person_id))
        connection.commit()

    print('Updated.')
    return True


def get(conditions):
    sql = f'''
SELECT * FROM phonebook_schema.persons WHERE {"AND".join([f"{pair[0]}='{pair[1]}'" for pair in conditions.items()])}
'''

    with connection.cursor() as cur:
        cur.execute(sql)
        persons = cur.fetchall()

    return persons


def delete(person_id):
    sql = f'''
DELETE FROM phonebook_schema.persons WHERE id = %s
'''

    with connection.cursor() as cur:
        cur.execute(sql, (person_id,))
        connection.commit()

    print('Deleted.')
    return True
