import asyncio
from taskorchestrator import TaskOrchestrator, Task

async def task_a():
    print("Task A started")
    await asyncio.sleep(2)
    return "Task A completed"

async def task_b():
    print("Task B started")
    await asyncio.sleep(1)
    return "Task B completed"

async def task_c():
    print("Task C started")
    await asyncio.sleep(3)
    return "Task C completed"

async def main():
    flow = TaskOrchestrator()
    task1 = Task(task_a)
    task2 = Task(task_b)
    task3 = Task(task_c)

    flow.add_tasks(task1, task2, task3)
    results = await flow.run_parallel()
    print(results)

asyncio.run(main())
