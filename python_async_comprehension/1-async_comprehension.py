#!/usr/bin/env python3
"""
Module for async comprehension that collects random numbers.
"""

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Uses async_generator to yield random numbers and collects them
    using async comprehension syntax.

    Returns:
        list: List of 10 random numbers between 0 and 10
    """
    async_generator = __import__('0-async_generator').async_generator
    return [number async for number in async_generator()]
 