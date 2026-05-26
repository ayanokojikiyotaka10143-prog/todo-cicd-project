import unittest
from io import StringIO
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()
    def test_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)
    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        open_titles = [task.title for task in open_tasks]
        self.assertIn("Create Dockerfile", open_titles)
        self.assertIn("Setup CI/CD Pipeline", open_titles)
        self.assertIn("Deploy Application", open_titles)
        self.assertEqual(len(open_tasks), 3)
    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        done_titles = [task.title for task in done_tasks]
        self.assertIn("Setup GitHub Repository", done_titles)
        self.assertIn("Develop Python Scripts", done_titles)
        self.assertIn("Write Unit Tests", done_titles)
        self.assertEqual(len(done_tasks), 3)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTaskPool)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    stream.seek(0)
    lines = stream.readlines()
    for line in lines:
        line = line.strip()
        if "..." in line and "ok" in line:
            print(line)
