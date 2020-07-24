import unittest
from model.yaml import Yaml
from model.environment import Environment

class TestYaml(unittest.TestCase):
    def test_when_define_environment_then_reflect_filename(self):
        file = Yaml(Environment.DEV)
        self.assertEqual('application-dev.yaml', file.name())

        file = Yaml(Environment.LOCAL)
        self.assertEqual('application-local.yaml', file.name())
