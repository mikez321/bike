"""Assert that tests can be run."""
from django.test import TestCase


class FirstTest(TestCase):
    """A test to test test cases."""

    def test_it_is_true(self):
        """True is always True."""
        self.assertTrue(True)
