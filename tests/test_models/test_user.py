import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.user import User


class test_User(test_basemodel):
    """Testing User class"""

    def test_inheritance(self):
        """Testing if User inherits from BaseModel"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_user = User()
        self.assertTrue(hasattr(new_user, 'email'))
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertTrue(hasattr(new_user, 'first_name'))
        self.assertTrue(hasattr(new_user, 'last_name'))
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_user = User()
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_user = User()
        self.assertEqual(str(new_user), "[User] ({}) {}".format(
            new_user.id, new_user.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue('__class__' in user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_user = User(email="test@example.com", password="password",
                        first_name="John", last_name="Doe")
        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "password")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
