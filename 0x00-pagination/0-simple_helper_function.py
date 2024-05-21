#!/usr/bin/env python3
"""
Task 0. Simple helper function

A function that returns a tuple of size two.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range

    This function return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in
    a list for those particular pagination parameters.

    Arguments:
        page (int): The number of pages to consider.
        page_size (int): The page size.

    Return:
        (tuple[int, int]): The start & end index matching to the pagination.
    """
    return ((page - 1) * page_size, page * page_size)