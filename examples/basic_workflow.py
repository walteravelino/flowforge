import asyncio
from taskorchestrator import TaskOrchestrator, Task

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    return {"data": [1, 2, 3]}

async def process_data(data):
    print("Processing data...")
    await asyncio.sleep(1)
    return [x * 2 for x in data["data"]]

async def save_results(results):
    print("Saving results...")
    await asyncio.sleep(1)
    return f"Results saved: {results}"

async def main():
    flow = TaskOrchestrator()
    task1 = Task(fetch_data, retries=3, timeout=5)
    task2 = Task(process_data, depends_on=[task1])
    task3 = Task(save_results, depends_on=[task2])

    flow.add_tasks(task1, task2, task3)
    results = await flow.run()
    print(results)

asyncio.run(main())
