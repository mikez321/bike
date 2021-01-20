"""Ensure working test environment."""

from django.test import TestCase


class SetupTest(TestCase):
    """Write a test and make sure it passes."""

    def test_it_works(self):
        """True is always True."""
        self.assertTrue(True)
