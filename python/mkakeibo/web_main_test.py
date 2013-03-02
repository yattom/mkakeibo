import unittest

from web_main import *

class IndexTest(unittest.TestCase):
    def test_get(self):
        target = Index()
        content = target.GET()
        self.assertIsNotNone(content)
