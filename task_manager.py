#Менеджер задач

#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __repr__(self):
        return f"{self.description} by {self.due_date} - {'Completed' if self.is_completed else 'Not Completed'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def display_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.is_completed]
        if current_tasks:
            print("Current Tasks:")
            for task in current_tasks:
                print(task)
        else:
            print("No current tasks.")
task_manager = TaskManager()
task_manager.add_task("Покупки", "2023-04-30")
task_manager.add_task("Встреча", "2023-05-01")

task_manager.display_current_tasks()

task_manager.mark_task_as_completed("Покупки")
task_manager.display_current_tasks()