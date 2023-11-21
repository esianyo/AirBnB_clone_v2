#!/usr/bin/python3
""" tests the state modole """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ function that tests the base model """

    def __init__(self, *args, **kwargs):
        """ method that creates a state """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ testing state element """
        new = self.value()
        self.assertEqual(type(new.name), str)
