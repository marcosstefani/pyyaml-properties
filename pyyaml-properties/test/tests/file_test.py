import unittest
from model.file import File
from model.environment import Environment

class TestFile(unittest.TestCase):
    def test_when_define_environment_then_reflect_filename(self):
        file = File(Environment.DEV)
        self.assertEqual('application-dev.yaml', file.name())

        file = File(Environment.LOCAL)
        self.assertEqual('application-local.yaml', file.name())