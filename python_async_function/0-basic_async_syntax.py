#!/usr/bin/env python3
"""
Module for basic async operations with random delays.
This module provides a coroutine that simulates asynchronous waiting
with random delay times for testing and learning purposes.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.
    
    Args:
        max_delay (int): Maximum delay time in seconds (default: 10)
        
    Returns:
        float: The actual delay time that was waited
    """
    # Generate a random delay between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    
    # Wait for the specified delay asynchronously
    await asyncio.sleep(delay)
    
    # Return the actual delay time that was waited
    return delay 