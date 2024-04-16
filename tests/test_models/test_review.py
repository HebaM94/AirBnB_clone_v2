import unittest
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.review import Review


class test_review(test_basemodel):
    """Testing Review class"""

    def test_inheritance(self):
        """Testing if Review inherits from BaseModel"""
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_attributes(self):
        """Testing attributes"""
        new_review = Review()
        self.assertTrue(hasattr(new_review, 'place_id'))
        self.assertTrue(hasattr(new_review, 'user_id'))
        self.assertTrue(hasattr(new_review, 'text'))
        self.assertEqual(new_review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")

    def test_attribute_types(self):
        """Testing types of attributes"""
        new_review = Review()
        self.assertIsInstance(new_review.place_id, str)
        self.assertIsInstance(new_review.user_id, str)
        self.assertIsInstance(new_review.text, str)

    def test_str_representation(self):
        """Testing __str__ method"""
        new_review = Review()
        self.assertEqual(str(new_review), "[Review] ({}) {}".format(
            new_review.id, new_review.__dict__))

    def test_to_dict_method(self):
        """Testing to_dict method"""
        new_review = Review()
        review_dict = new_review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertTrue('__class__' in review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_initialization(self):
        """Testing if attributes are initialized"""
        new_review = Review(place_id="123", user_id="456",
                            text="Best Stay Ever!")
        self.assertEqual(new_review.place_id, "123")
        self.assertEqual(new_review.user_id, "456")
        self.assertEqual(new_review.text, "Best Stay Ever!")


if __name__ == '__main__':
    unittest.main()
