#!/usr/bin/env python3
"""
Module for executing multiple asyncio tasks concurrently.
This module provides functionality to run multiple tasks
simultaneously and collect their results in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple task_wait_random tasks concurrently.

    Args:
        n (int): Number of tasks to execute
        max_delay (int): Maximum delay time for each task

    Returns:
        List[float]: List of delay times in ascending order
    """
    # Create tasks for all coroutines
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collect results as they complete (naturally in ascending order)
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)

    return delays
