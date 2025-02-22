# Quick Start

## Installation
```bash
pip install flowforge
```

Basic Usage

```python
import asyncio
from flowforge import FlowForge, Task


async def fetch_data():
    return {"data": [1, 2, 3]}


async def process_data(data):
    return [x * 2 for x in data["data"]]


flow = FlowForge()
task1 = Task(fetch_data)
task2 = Task(process_data, depends_on=[task1])

flow.add_tasks(task1, task2)

results = await flow.run()

print(results)
``` 