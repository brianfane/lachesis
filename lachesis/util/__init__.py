r"""
Utilities for the lachesis module.
"""
import pickle

def load_data():
    r"""
    Load any saved data.
    """
    with open('lachesis.data', 'rb') as save_data:
        data = pickle.load(save_data)
    return data
