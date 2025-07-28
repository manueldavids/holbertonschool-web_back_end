# Python - Async

## Project Overview

This project focuses on Python asynchronous programming concepts, specifically exploring the `async` and `await` syntax, coroutines, tasks, and concurrent execution patterns. The project consists of five progressive tasks that build upon each other to demonstrate various aspects of asynchronous programming in Python.

## Learning Objectives

Upon completion of this project, students will be able to explain to anyone, without external assistance:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module in async contexts

## Project Structure

### Task 0: The basics of async
**File:** `0-basic_async_syntax.py`

Implementation of a basic asynchronous coroutine `wait_random` that:
- Takes an integer argument `max_delay` (default: 10)
- Waits for a random delay between 0 and `max_delay` seconds
- Returns the actual delay time as a float
- Uses the `random` module for delay generation

**Key Concepts:**
- Basic coroutine definition with `async def`
- `await` keyword for non-blocking operations
- `asyncio.sleep()` for asynchronous waiting
- Type hints and documentation requirements

### Task 1: Let's execute multiple coroutines at the same time with async
**File:** `1-concurrent_coroutines.py`

Implementation of `wait_n` function that:
- Executes `wait_random` n times with specified `max_delay`
- Runs all coroutines concurrently
- Returns delays in ascending order without using `sort()`
- Leverages natural completion order for sorting

**Key Concepts:**
- `asyncio.as_completed()` for handling completion order
- Concurrent execution of multiple coroutines
- List comprehensions with async operations
- Importing functions from previous modules

### Task 2: Measure the runtime
**File:** `2-measure_runtime.py`

Implementation of `measure_time` function that:
- Measures total execution time for `wait_n(n, max_delay)`
- Returns average time per coroutine (`total_time / n`)
- Uses the `time` module for precise timing
- Demonstrates synchronous function calling async code

**Key Concepts:**
- `asyncio.run()` for executing coroutines from sync functions
- Time measurement with `time.time()`
- Performance benchmarking
- Function composition with async operations

### Task 3: Tasks
**File:** `3-tasks.py`

Implementation of `task_wait_random` function that:
- Creates an `asyncio.Task` from `wait_random` coroutine
- Uses regular function syntax (not async)
- Returns a Task object for better control
- Demonstrates task creation and management

**Key Concepts:**
- `asyncio.create_task()` for task creation
- Difference between coroutines and tasks
- Task lifecycle and management
- Type annotations with `asyncio.Task`

### Task 4: Tasks
**File:** `4-tasks.py`

Implementation of `task_wait_n` function that:
- Modifies `wait_n` to use `task_wait_random` instead of `wait_random`
- Executes multiple tasks concurrently
- Maintains ascending order results
- Demonstrates task-based concurrency

**Key Concepts:**
- Task-based concurrent execution
- Evolution from coroutines to tasks
- Enhanced control and monitoring capabilities
- Consistent API with improved performance characteristics

## Technical Requirements

### Code Standards
- All files must be executable
- All files must end with a new line
- All functions and coroutines must be type-annotated
- All modules must have proper documentation
- Code must pass `pycodestyle` (version 2.5.x)

### Python Environment
- Python 3.9 on Ubuntu 20.04 LTS
- Standard library modules: `asyncio`, `random`, `time`, `typing`

### File Structure
```
python_async_function/
├── README.md
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
└── 4-tasks.py
```

## Usage Examples

### Basic Async Coroutine
```python
import asyncio
from 0-basic_async_syntax import wait_random

# Execute with default max_delay (10)
result = asyncio.run(wait_random())
print(result)  # Random float between 0 and 10

# Execute with custom max_delay
result = asyncio.run(wait_random(5))
print(result)  # Random float between 0 and 5
```

### Concurrent Execution
```python
import asyncio
from 1-concurrent_coroutines import wait_n

# Execute 5 coroutines with max_delay of 5
results = asyncio.run(wait_n(5, 5))
print(results)  # List of 5 floats in ascending order
```

### Performance Measurement
```python
from 2-measure_runtime import measure_time

# Measure average time per coroutine
avg_time = measure_time(5, 9)
print(avg_time)  # Average execution time per coroutine
```

### Task Creation
```python
import asyncio
from 3-tasks import task_wait_random

async def test():
    task = task_wait_random(5)
    result = await task
    print(task.__class__)  # <class '_asyncio.Task'>

asyncio.run(test())
```

## Key Learning Outcomes

### Asynchronous Programming Fundamentals
- Understanding of event-driven programming
- Non-blocking I/O operations
- Cooperative multitasking with coroutines

### Concurrency Patterns
- Sequential vs concurrent execution
- Task scheduling and management
- Performance optimization through concurrency

### Python Async Ecosystem
- `asyncio` library usage
- Best practices for async code
- Integration with synchronous code

### Code Quality
- Type annotations in async contexts
- Documentation standards
- Code style compliance

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Author

This project is part of the Holberton School curriculum, focusing on advanced Python programming concepts and asynchronous execution patterns.