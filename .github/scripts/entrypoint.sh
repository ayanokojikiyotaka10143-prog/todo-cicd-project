#!/bin/bash
echo "=== Running Task Manager ==="
echo "Running todo.py..."
python3 /app/.github/scripts/todo.py | tee /app/todo_output.txt
echo ""
echo "Running todo-test.py..."
python3 /app/.github/scripts/todo-test.py | tee /app/test_output.txt
echo ""
echo "Updating index.html..."
bash /app/.github/scripts/update_index.sh /app/todo_output.txt /app/test_output.txt
echo ""
echo "=== All tasks completed ==="
