#!/usr/bin/env python3
"""
Module for summing list of floats with type annotations.
This module provides a type-annotated function to sum a list of float numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum all float numbers in a list and return the result.

    Args:
        input_list (List[float]): The list of float numbers to sum

    Returns:
        float: The sum of all numbers in the list
    """
    return sum(input_list)
