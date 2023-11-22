r"""
Utilities for the lachesis module.
"""
import pickle
import logging
import typing
import inspect
from pprint import pformat

DEBUG_LEVEL = logging.CRITICAL
DEBUG_FORMAT = '%(asctime)s: (%(levelname)s) %(name)s():\n\t%(message)s'
logging.basicConfig(format=DEBUG_FORMAT,
                    encoding='utf-8',
                    level=DEBUG_LEVEL)

def create_logger(logger_name: str) -> logging.Logger:
    r"""
    Create a logger.
    """
    logger = logging.getLogger(logger_name)
    return logger

def initialize_data() -> dict:
    r"""
    Initialize our data because we didn't find anything.
    """
    logger = create_logger('util.initialize_data')
    logger.debug('start')
    data = {'timeslices': [],
            'events': []
            }
    logger.debug('ending')
    return data

def load_data():
    r"""
    Load any saved data.
    """
    logger = create_logger('util.create_logger')
    logger.debug('starting')
    try:
        with open('lachesis.data', 'rb') as save_data:
            logger.debug('un-pickling data')
            data = pickle.load(save_data)
        logger.debug('returning data')
        return data
    except FileNotFoundError:
        logger.debug('no data found; initializing data')
        return initialize_data()
