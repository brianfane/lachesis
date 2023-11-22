r"""
Tests for the Categories class
"""

import unittest
from lachesis.categories import Categories

class TestCategories(unittest.TestCase):
    r"""
    Tests for the Categories class
    """
    def test_categories(self):
        r"""
        Test creating a Categories object.
        """
        cats = Categories()
        self.assertIsInstance(cats, Categories)

    def test_getitem(self):
        r"""
        Test the __getitem__() method;
        """
        cats = Categories()
        cats.add_category('Category 1')
        cats.add_category('Category 2')
        cats.add_category('Category 3')
        #
        # Test by category ID
        found_cat = cats[1]
        self.assertIsInstance(found_cat, str)
        self.assertEqual(found_cat, 'Category 2')
        #
        # Test by string
        found_cat = cats['Category 3']
        self.assertIsInstance(found_cat, int)
        self.assertEqual(found_cat, 2)
        found_cat = cats['Category 1']
        self.assertIsInstance(found_cat, int)
        self.assertEqual(found_cat, 0)

    def test_add_category(self):
        r"""
        Test the add_category() and __len__() methods
        """
        cats = Categories()
        self.assertEqual(len(cats), 0)
        cats.add_category('Category 1')
        self.assertEqual(len(cats), 1)
        cats.add_category('Category 2')
        self.assertEqual(len(cats), 2)

    def test_iter(self):
        r"""
        Test the __iter__() method
        """
        cats = Categories()
        cats.add_category('Category 1')
        cats.add_category('Category 2')
        cats.add_category('Category 3')
        expected_cat_id = 0
        for cat_id in cats:
            self.assertIsInstance(cat_id, int)
            self.assertEqual(cat_id, expected_cat_id)
            expected_cat_id += 1
