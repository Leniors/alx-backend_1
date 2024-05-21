#!/usr/bin/env python3
"""
Task 1. Simple pagination

Implemented get_page which returns the pages in the dataset.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page

        This function returns the pages in the dataset inputed by
        the parameters.

        Arguments:
            page (int): The page numbers. Default to 1.
            page_size (int): The page size. Default to 10.

        Return:
            (List[List]): The pages to be returned.
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start:end]