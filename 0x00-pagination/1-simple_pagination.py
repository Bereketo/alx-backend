#!/usr/bin/env python3
"""simple pagination
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two containing a start index and an end index
    """
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


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
        """Returns records of a page
        """
        data = []
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        start, end = index_range(page, page_size)
        index = 0
        returned = self.dataset()
        if start > len(returned):
            return []
        while start < end:
            data.append(returned[start])
            index += 1
            start += 1
        return data
