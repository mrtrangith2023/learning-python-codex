# Bài 12: Mini To-Do App
# tasks = []

# Cho phép:

# tasks.append("Learn Python")
# tasks.append("Learn Git")
# tasks.append("Build AI Project")

# In:

# 1. Learn Python
# 2. Learn Git
# 3. Build AI Project
tasks = []

tasks.append("Learn Python")
tasks.append("Learn Git")
tasks.append("Build AI Project")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")