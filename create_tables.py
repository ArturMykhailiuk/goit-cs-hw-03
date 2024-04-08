import psycopg2

# Параметри підключення
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
# читаємо файл зі скриптом для створення БД
    with open('manage_tasks.sql', 'r') as f:
        sql = f.read()
    try:
        cursor.execute(sql)
        connection.commit()
    except (Exception, psycopg2.Error) as commit_error:
        print("Помилка при виконанні запитів:", commit_error)
        connection.rollback() # Відкатити зміни у випадку помилки

    
    # Виконання запитів та інших операцій з базою даних
    
except (Exception, psycopg2.Error) as connection_error:
    print("Помилка при підключенні до PostgreSQL:", connection_error)
finally:
    # Закриття з'єднання
    if (connection):
        cursor.close()
        connection.close()
        print("З'єднання з PostgreSQL закрито")


