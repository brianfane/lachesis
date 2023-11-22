r"""
categories.py
"""

from collections.abc import Mapping
from lachesis.util import create_logger

class Categories(Mapping):
    r"""
    Categories that we can assign time to.
    """
    def __init__(self):
        logger = create_logger('Categories.__init__')
        logger.debug('starting')
        self.__categories = {}
        logger.debug('ending')

    def add_category(self, category_name: str) -> None:
        r"""
        Add a category to our list.
        """
        logger = create_logger('Categories.add_category')
        logger.debug('starting')
        self.__categories[len(self)] = category_name
        logger.debug('ending')

    def items(self):
        logger = create_logger('Categories.items()')
        logger.debug('starting')
        for cat_tuple in self.__categories:
            yield cat_tuple

    def __getitem__(self, item_key):
        logger = create_logger('Categories.__getitem__')
        logger.debug('starting')
        if isinstance(item_key, int):
            logger.debug('item_key is a integer; returning specific entry')
            return self.__categories[item_key]
        if isinstance(item_key, str):
            logger.debug('item_key is a string; finding the category')
            for cat_id, cat_name in self.__categories.items():
                logger.debug(f'cat_id = {cat_id}; cat_name = "{cat_name}"')
                if cat_name == item_key:
                    logger.debug(f'category found; {cat_id}')
                    return cat_id
            else:
                logger.debug('category not found; throwing an exception')
                raise KeyError
        logger.debug('the wrong data type used for a key; throwing exception')
        raise ValueError

    def __iter__(self):
        logger = create_logger('Categories.__iter__')
        logger.debug('starting')
        start_id = 0
        curr_id = start_id
        while curr_id < len(self):
            if curr_id in self.__categories:
                yield curr_id
            curr_id += 1
        logger.debug('ending')

    def __len__(self):
        logger = create_logger('Categories.__len__')
        logger.debug('starting')
        return len(self.__categories)
