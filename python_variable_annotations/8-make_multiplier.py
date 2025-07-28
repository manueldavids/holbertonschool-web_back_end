#!/usr/bin/env python3
"""
Module for creating multiplier functions with type annotations.
This module provides a type-annotated function that returns a multiplier
function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product with the multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
