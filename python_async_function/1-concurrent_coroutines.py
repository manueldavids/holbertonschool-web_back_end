#!/usr/bin/env python3
"""
Module for executing multiple coroutines concurrently.
This module provides functionality to run multiple async operations
simultaneously and collect their results in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple wait_random coroutines concurrently.

    Args:
        n (int): Number of coroutines to execute
        max_delay (int): Maximum delay time for each coroutine

    Returns:
        List[float]: List of delay times in ascending order
    """
    # Create tasks for all coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Collect results as they complete (naturally in ascending order)
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)

    return delays
