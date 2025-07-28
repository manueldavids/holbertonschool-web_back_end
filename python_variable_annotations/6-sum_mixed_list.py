#!/usr/bin/env python3
"""
Module for summing mixed list of integers and floats with type annotations.
This module provides a type-annotated function to sum a list of mixed numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all numbers (integers and floats) in a list and return the result.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed numbers to sum

    Returns:
        float: The sum of all numbers in the list
    """
    return sum(mxd_lst)
