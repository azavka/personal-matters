import datetime

# Создать функцию для получения ввода от пользователя
def get_user_input():
    # Получить название задачи
    task_name = input("Введите название задачи: ")

    # Получить дату выполнения задачи
    task_date = input("Введите дату выполнения задачи (ГГГГ-ММ-ДД): ")
    task_date = datetime.datetime.strptime(task_date, "%Y-%m-%d")

    # Получить приоритет задачи
    task_priority = input("Введите приоритет задачи (1-5): ")
    task_priority = int(task_priority)

    # Вернуть введенные данные
    return task_name, task_date, task_priority

# Создать функцию для добавления задачи в список
def add_task(task_list, task_name, task_date, task_priority):
    # Создать словарь для новой задачи
    new_task = {
        "task_name": task_name,
        "task_date": task_date,
        "task_priority": task_priority
    }

    # Добавить новую задачу в список
    task_list.append(new_task)

# Создать функцию для печати списка задач
def print_task_list(task_list):
    # Отсортировать список задач по дате и приоритету
    task_list.sort(key=lambda task: (task["task_date"], task["task_priority"]))

    # Напечатать список задач
    for task in task_list:
        print(f"Задача: {task['task_name']}")
        print(f"Дата выполнения: {task['task_date']}")
        print(f"Приоритет: {task['task_priority']}")
        print()

# Создать список задач
task_list = []

# Получить ввод от пользователя и добавить задачи в список
while True:
    # Получить ввод от пользователя
    task_name, task_date, task_priority = get_user_input()

    # Добавить задачу в список
    add_task(task_list, task_name, task_date, task_priority)

    # Спросить пользователя, хочет ли он добавить еще одну задачу
    add_another_task = input("Хотите добавить еще одну задачу? (y/n): ")
    if add_another_task == "n":
        break

# Напечатать список задач
print_task_list(task_list)
input()
