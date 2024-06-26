class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Not completed"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Completed"
                return  # Выходим из метода после установки статуса

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "Not completed"]
        return current_tasks

task_manager = TaskManager()

task1 = Task("Позвонить маме", "26.06.2024")
task2 = Task("Сходить в магазин", "26.06.2024")

task_manager.add_task(task1)
task_manager.add_task(task2)

task_manager.mark_task_as_completed("Позвонить маме")

current_tasks = task_manager.get_current_tasks()
for task in current_tasks:
    print(f"Описание: {task.description}, Срок выполнения: {task.deadline}, Статус: {task.status}")