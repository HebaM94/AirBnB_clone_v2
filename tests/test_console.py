import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the HBNB console"""
        self.console = HBNBCommand()
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Clean up after each test"""
        sys.stdout = self.stdout

    def test_create(self):
        """Test the create command"""
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel", sys.stdout.getvalue())

    def test_show(self):
        """Test the show command"""
        self.console.onecmd("create BaseModel")
        obj_id = sys.stdout.getvalue().strip()
        sys.stdout = StringIO()
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn(obj_id, sys.stdout.getvalue())

    def test_destroy(self):
        """Test the destroy command"""
        self.console.onecmd("create BaseModel")
        obj_id = sys.stdout.getvalue().strip()
        sys.stdout = StringIO()
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.assertNotIn(obj_id, sys.stdout.getvalue())

    def test_all(self):
        """Test the all command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")
        sys.stdout = StringIO()
        self.console.onecmd("all")
        self.assertIn("BaseModel", sys.stdout.getvalue())
        self.assertIn("User", sys.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
