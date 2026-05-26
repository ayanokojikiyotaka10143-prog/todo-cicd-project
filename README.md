# Task Manager CI/CD Pipeline
Python task management system with automated CI/CD using GitHub Actions and Docker.

## Running Locally
```
python3 .github/scripts/todo.py
python3 .github/scripts/todo-test.py
```

## Running with Docker
```
docker build -t task-manager:latest .
docker run --rm task-manager:latest
```

## Author
Hasibul Islam Shihab — 14607889 — UTS
