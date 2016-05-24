
import sys
import unittest
from travis_tests.tclass import TClass


class TravisTestsTests(unittest.TestCase):
    """Tests TravisTests class."""

    @classmethod
    def setUpClass(cls):
        """Test setUp method."""
        pass

    @classmethod
    def tearDownClass(cls):
        """Test tearDown method."""
        pass

    def test_funca(self):
        """Test funcA function"""
        c = TClass()
        self.assertEquals(c.funcA(), 'A')

    def test_funcb(self):
        """Test funcB function"""
        c = TClass()
        self.assertEquals(c.funcB(), 'B')

    def test_funcb_fails(self):
        """Test funcB function fails"""
        c = TClass()
        self.assertNotEqual(c.funcB(), '')

    def test_QGIS_is_available(self):
        """Test QGIS bindings can be imported"""
        try:
            from qgis import core
        except ImportError:
            self.fail("QGIS binding are not available")


class TravisTestsFailsTests(unittest.TestCase):
    """Tests TravisTests class."""

    def test_funcb_fails(self):
        """Test funcB function fails"""
        c = TClass()
        self.assertEqual(c.funcB(), '')

class TravisTestsPythonEerror(unittest.TestCase):
    """Tests a python error."""

    def test_python_error(self):
        """Test a python error"""
        self.assertTrue(this_var_is_not_defined)


def suite():
    suite = unittest.makeSuite(TravisTestsTests, 'test')
    return suite

# run all tests using unittest skipping nose or testplugin
def run_all():
    # demo_test = unittest.TestLoader().loadTestsFromTestCase(CatalogTests)
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())

# run all failing tests using unittest skipping nose or testplugin
def run_fail():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(unittest.makeSuite(TravisTestsFailsTests, 'test'))

# I want a python error here
def run_python_error():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(unittest.makeSuite(TravisTestsPythonEerror, 'test_err'))


if __name__ == "__main__":
    run_all()
