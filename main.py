#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# #Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        self.status = True

    def is_done(self):
        return self.status

tasks = []

def add_task(description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def display_current_tasks():
    print("Текущие задачи:")
    for task in tasks:
        if not task.is_done():
            print(f"Описание: {task.description}, Срок выполнения: {task.deadline}, Статус: {'Выполнено' if task.is_done() else 'Не выполнено'}")

# Пример использования:
add_task("Подготовить отчет", "30.03.2024")
add_task("Составить план работы", "05.04.2024")
add_task("Провести совещание", "10.04.2024")

tasks[0].mark_as_done()

display_current_tasks()


