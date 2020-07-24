import unittest

from .tests import file_test

loader = unittest.TestLoader
suite = unittest.TestSuite

suite.addTest(loader.loadTestsFromModule(file_test))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)