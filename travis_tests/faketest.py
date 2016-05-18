# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
import unittest
import os
import sys
from qgis.core import *
from qgis.utils import iface
from PyQt4.QtCore import *
import re

class FakeTests(unittest.TestCase):
    '''
    '''

    @classmethod
    def setUpClass(cls):
        ''' 'test' workspace cannot exist in the test catalog'''
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testPasses(self):
        self.assertTrue(True)

    def ______testFails(self):
        self.assertTrue(False)

    def testPasses2(self):
        self.assertTrue(True)


##################################################################################################

def suite():
    suite = unittest.makeSuite(FakeTests, 'test')
    return suite

# run all tests using unittest skipping nose or testplugin
def run_all():
    # demo_test = unittest.TestLoader().loadTestsFromTestCase(CatalogTests)
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())


def run_sleep():
    from time import sleep
    sleep(5)

if __name__ == "__main__":
    run_all()
