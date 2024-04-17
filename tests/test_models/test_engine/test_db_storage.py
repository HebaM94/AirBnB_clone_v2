import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models import storage
import os


class TestDBStorage(unittest.TestCase):
    """ Class to test the db storage method """
    def setUp(self):
        """Set up the DBStorage"""
        self.db_storage = DBStorage()

    def tearDown(self):
        """Clean up after each test"""
        storage.reload()

    def test_all_method(self):
        """Test the all method"""
        new_obj = BaseModel()
        new_obj.save()
        obj_dict = storage.all()
        self.assertIn(new_obj, obj_dict.values())

    
if __name__ == '__main__':
    unittest.main()
