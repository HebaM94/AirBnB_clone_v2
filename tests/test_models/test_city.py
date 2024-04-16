import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.city import City


class test_City(test_basemodel):
    """Testing City class"""

    def test_inheritance(self):
        """Testing if City inherits from BaseModel"""
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_city = City()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_city = City()
        self.assertIsInstance(new_city.state_id, str)
        self.assertIsInstance(new_city.name, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_city = City()
        self.assertEqual(str(new_city), "[City] ({}) {}".format(
            new_city.id, new_city.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_city = City()
        city_dict = new_city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertTrue('__class__' in city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_city = City(state_id="NY", name="New York")
        self.assertEqual(new_city.state_id, "NY")
        self.assertEqual(new_city.name, "New York")


if __name__ == '__main__':
    unittest.main()
