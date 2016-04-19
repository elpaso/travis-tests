
import unittest
from travis_tests import TravisTests


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
        c = TravisTests()
        self.assertEquals(c.funcA(), 'A')

    def test_funcb(self):
        """Test funcB function"""
        c = TravisTests()
        self.assertEquals(c.funcB(), 'B')

    def test_funcb_fails(self):
        """Test funcB function fails"""
        c = TravisTests()
        self.assertNotEqual(c.funcB(), '')

    def test_QGIS_is_available(self):
        """Test QGIS bindings can be imported"""
        try:
            from qgis import core
        except ImportError:
            self.fail("QGIS binding are not available")
