#!/usr/bin/env python3
"""
Module for element length function with type annotations.
This module provides a type-annotated function to get element lengths from
iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Create a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (strings, lists,
        etc.)

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with (element, length)
    """
    return [(i, len(i)) for i in lst]
