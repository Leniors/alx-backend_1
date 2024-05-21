#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index

        This method that takes 2 arguments and returns a key_value pair

        Arguments:
            index (int): The current starting index of the page to return.
                        Default value None.
            page_size (int): The size of the pages. Default value 10.

        Return:
            (Dict): A dictionary of key value pairs.
        """
        if index is None:
            index = 0
        assert (isinstance(index, int))
        assert (index > 0 and index < len(self.__indexed_dataset))

        sorted_data = self.indexed_dataset()
        data = []
        current_index = index
        while len(data) < page_size and current_index < len(sorted_data):
            item = sorted_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1
        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }