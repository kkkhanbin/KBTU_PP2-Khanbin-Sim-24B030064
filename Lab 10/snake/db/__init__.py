from .config import load_config
from .db import connect

connection = connect(load_config('db/database.ini'))
table_name = ""


def insert(persons):
    sql = '''
INSERT INTO snake.snake(nickname, level, score)
VALUES(%s, %s, %s) RETURNING *;
'''

    with connection.cursor() as cur:
        print(cur.executemany(sql, persons))
        connection.commit()

    print('Created.')
    return True


def update(person_id, person):
    sql = '''
UPDATE snake.snake
SET nickname = %s, score = %s, level = %s
WHERE id = %s
'''

    with connection.cursor() as cur:
        cur.execute(sql, (*person, person_id))
        connection.commit()

    # print('Updated.')
    return True


def get(conditions):
    sql = f'''
SELECT * FROM snake.snake WHERE {"AND".join([f"{pair[0]}='{pair[1]}'" for pair in conditions.items()])}
'''

    with connection.cursor() as cur:
        cur.execute(sql)
        persons = cur.fetchall()

    return persons


def delete(person_id):
    sql = f'''
DELETE FROM snake.snake WHERE id = %s
'''

    with connection.cursor() as cur:
        cur.execute(sql, (person_id,))
        connection.commit()

    print('Deleted.')
    return True
