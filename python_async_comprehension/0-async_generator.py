#!/usr/bin/env python3
"""
Module for async generator that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields 10 random numbers between 0 and 10.

    Each iteration waits 1 second asynchronously before yielding.

    Yields:
        float: Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)