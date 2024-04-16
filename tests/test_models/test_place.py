import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.place import Place


class test_Place(test_basemodel):
    """Testing Place class"""

    def test_inheritance(self):
        """Testing if Place inherits from BaseModel"""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_place = Place()
        self.assertTrue(hasattr(new_place, 'city_id'))
        self.assertTrue(hasattr(new_place, 'user_id'))
        self.assertTrue(hasattr(new_place, 'name'))
        self.assertTrue(hasattr(new_place, 'description'))
        self.assertTrue(hasattr(new_place, 'number_rooms'))
        self.assertTrue(hasattr(new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(new_place, 'max_guest'))
        self.assertTrue(hasattr(new_place, 'price_by_night'))
        self.assertTrue(hasattr(new_place, 'latitude'))
        self.assertTrue(hasattr(new_place, 'longitude'))
        self.assertTrue(hasattr(new_place, 'amenity_ids'))
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_place = Place()
        self.assertIsInstance(new_place.city_id, str)
        self.assertIsInstance(new_place.user_id, str)
        self.assertIsInstance(new_place.name, str)
        self.assertIsInstance(new_place.description, str)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertIsInstance(new_place.latitude, float)
        self.assertIsInstance(new_place.longitude, float)
        self.assertIsInstance(new_place.amenity_ids, list)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_place = Place()
        self.assertEqual(str(new_place), "[Place] ({}) {}".format(
            new_place.id, new_place.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_place = Place()
        place_dict = new_place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertTrue('__class__' in place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_place = Place(city_id="NY", user_id="user1", name="Cozy Home",
                          description="Amazing small home", number_rooms=2,
                          number_bathrooms=2, max_guest=4, price_by_night=110,
                          latitude=42.8126, longitude=-69.0040,
                          amenity_ids=["wifi", "pool"])
        self.assertEqual(new_place.city_id, "NY")
        self.assertEqual(new_place.user_id, "user1")
        self.assertEqual(new_place.name, "Cozy Home")
        self.assertEqual(new_place.description, "Amazing small home")
        self.assertEqual(new_place.number_rooms, 2)
        self.assertEqual(new_place.number_bathrooms, 2)
        self.assertEqual(new_place.max_guest, 4)
        self.assertEqual(new_place.price_by_night, 110)
        self.assertEqual(new_place.latitude, 42.8126)
        self.assertEqual(new_place.longitude, -69.0040)
        self.assertEqual(new_place.amenity_ids, ["wifi", "pool"])


if __name__ == '__main__':
    unittest.main()
