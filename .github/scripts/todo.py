class Task:
    def __init__(self, title, status="ToDo", priority="Medium"):
        self.title = title
        self.completed = False
        self.status = status
        self.priority = priority
    def mark_completed(self):
        self.completed = True
        self.status = "Done"
    def __repr__(self):
        return f"{self.title} - {self.status}"
    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"

class TaskPool:
    def __init__(self):
        self.tasks = []
    def populate(self):
        task1 = Task("Setup GitHub Repository")
        task2 = Task("Develop Python Scripts")
        task3 = Task("Write Unit Tests")
        task4 = Task("Create Dockerfile")
        task5 = Task("Setup CI/CD Pipeline")
        task6 = Task("Deploy Application")
        task1.mark_completed()
        task2.mark_completed()
        task3.mark_completed()
        self.tasks = [task1, task2, task3, task4, task5, task6]
    def add_task(self, task):
        self.tasks.append(task)
    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]
    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]

def main():
    pool = TaskPool()
    pool.populate()
    todo_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in todo_titles:
        print(f"  {title}")
    done_titles = [task.title for task in pool.get_done_tasks()]
    print("Done Tasks:")
    for title in done_titles:
        print(f"  {title}")

if __name__ == "__main__":
    main()
