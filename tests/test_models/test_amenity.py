import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Testing Amenity class"""

    def test_inheritance(self):
        """Testing if Amenity inherits from BaseModel"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, 'name'))
        self.assertEqual(new_amenity.name, '')

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity.name, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_amenity = Amenity()
        self.assertEqual(str(new_amenity), "[Amenity] ({}) {}".format(
            new_amenity.id, new_amenity.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_amenity = Amenity()
        amenity_dict = new_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertTrue('__class__' in amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_amenity = Amenity(name="test_name")
        self.assertEqual(new_amenity.name, "test_name")


if __name__ == '__main__':
    unittest.main()
