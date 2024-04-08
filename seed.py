from datetime import datetime
import faker
from random import randint, choice
import psycopg2

NUMBER_USERS = 5
NUMBER_STATUSES = 3
NUMBER_TASKS = 10

def generate_fake_data(number_users, number_statuses, number_tasks) -> tuple:
    fake_users = []
    fake_emails = []
    statuses = []
    fake_title=[]
    fake_description=[]

    fake_data = faker.Faker()
    
    default_statuses = ['new', 'in progress', 'completed']

# Створимо набір users в кількості number_users
    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

#Створимо набір status в кількості number_statuses з визанченого списку статусів
    for status in default_statuses:
        statuses.append(status)

# Та number_tasks набір завдань
    for _ in range(number_tasks):
        fake_title.append(fake_data.word())
        fake_description.append(fake_data.text())


    return fake_users, fake_emails, statuses, fake_title, fake_description

def prepare_data(users, emails, statuses, titles, descriptions) -> tuple:
    for_users = []
# Готуємо список кортежів імен і пошти
    for user, email in zip(users, emails):
        for_users.append((user, email))

# Готуємо список кортежів статусів
    for_statuses = []
    for status in statuses:
        for_statuses.append((status,))

# Готуємо список кортежів завдань    
    for_tasks = []
    for title, description in zip(titles, descriptions):
        for_tasks.append((title, description,randint(1, NUMBER_USERS), randint(1, NUMBER_STATUSES)))
    return for_users, for_statuses, for_tasks

def insert_data_to_db(users, statuses, tasks) -> None:
# Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними

    parametri = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "18764505"
}

# Встановлення з'єднання
    try:
        connection = psycopg2.connect(**parametri)
        cursor = connection.cursor()
        print("Підключено до PostgreSQL")

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (%s, %s)"""

        cursor.executemany(sql_to_users, users)
  

        sql_to_statuses = """INSERT INTO status(name)
                               VALUES (%s)"""

        cursor.executemany(sql_to_statuses, statuses)
        
  
        sql_to_tasks = """INSERT INTO tasks(title, description, user_id, status_id)
                              VALUES (%s, %s, %s, %s)"""

        cursor.executemany(sql_to_tasks, tasks)

        connection.commit()

    except (Exception, psycopg2.Error) as commit_error:
        print("Помилка при виконанні запитів:", commit_error)
        connection.rollback() # Відкотити зміни у випадку помилки

if __name__ == "__main__":
    users, statuses, tasks = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_STATUSES, NUMBER_TASKS))
    print(users)
    insert_data_to_db(users, statuses, tasks)