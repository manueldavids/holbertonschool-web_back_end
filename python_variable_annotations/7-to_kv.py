#!/usr/bin/env python3
"""
Module for creating key-value tuple with type annotations.
This module provides a type-annotated function to create a tuple with key and
squared value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string key and the square of a number as float.

    Args:
        k (str): The string key
        v (Union[int, float]): The number to square

    Returns:
        Tuple[str, float]: A tuple containing the key and squared value
    """
    return (k, v * v)
