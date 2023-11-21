#!/usr/bin/python3
""" tests the amenities model """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ main test function """

    def __init__(self, *args, **kwargs):
        """ test method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ name test """
        new = self.value()
        self.assertEqual(type(new.name), str)
