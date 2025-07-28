#!/usr/bin/env python3
"""
Module for floor function with type annotations.
This module provides a type-annotated function to get the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Get the floor (largest integer less than or equal to) of a float number.

    Args:
        n (float): The float number to get the floor of

    Returns:
        int: The floor of the float number
    """
    return math.floor(n)
