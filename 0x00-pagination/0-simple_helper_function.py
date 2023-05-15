#!/usr/bin/env python3
"""contains a function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a
        list for those particular pagination parameters.
    """
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
