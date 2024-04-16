import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.state import State


class test_state(test_basemodel):
    """Testing State class"""

    def test_inheritance(self):
        """Testing if State inherits from BaseModel"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_state = State()
        self.assertTrue(hasattr(new_state, 'name'))
        self.assertEqual(new_state.name, "")

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_state = State()
        self.assertIsInstance(new_state.name, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_state = State()
        self.assertEqual(str(new_state), "[State] ({}) {}".format(
            new_state.id, new_state.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_state = State()
        state_dict = new_state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertTrue('__class__' in state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_state = State(name="California")
        self.assertEqual(new_state.name, "California")


if __name__ == '__main__':
    unittest.main()
