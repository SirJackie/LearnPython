import unittest
from MyDict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        # This Function will run before every Test Case
        print("setUp...")

    def tearDown(self):
        # This Function will run after every Test Case
        print("tearDown...")

    def test_init(self):
        d = Dict(a=123, b="Test")
        self.assertEqual(d.a, 123)
        self.assertEqual(d.b, "Test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == "__main__":
    unittest.main()

# Or use Terminal to do this test:
# python -m unittest UnitTest.py
