#!/usr/bin/env python3
"""
Module for measuring execution time of concurrent coroutines.
This module provides functionality to benchmark the performance
of async operations and calculate average execution times.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines to execute
        max_delay (int): Maximum delay time for each coroutine

    Returns:
        float: Average time per coroutine (total_time / n)
    """
    # Record start time
    start_time = time.time()

    # Execute wait_n and wait for completion
    asyncio.run(wait_n(n, max_delay))

    # Record end time
    end_time = time.time()

    # Calculate total execution time
    total_time = end_time - start_time

    # Return average time per coroutine
    return total_time / n
