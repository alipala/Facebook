import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Tests.test_login import TestLogin
from Tests.test_register import TestRegister
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(TestLogin))
suite.addTest(loader.loadTestsFromModule(TestRegister))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)