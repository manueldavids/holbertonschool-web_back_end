#!/usr/bin/env python3
"""
Module for creating asyncio tasks from coroutines.
This module provides functionality to wrap coroutines in tasks
for better control and management of async operations.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task from wait_random coroutine.

    Args:
        max_delay (int): Maximum delay time for the coroutine

    Returns:
        asyncio.Task: Task object representing the coroutine execution
    """
    # Create and return a task from the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))
