# unittest_skip.py

import sys
import unittest


class SkippingTest(unittest.TestCase):

    @unittest.skip('sempre saltati')
    def test(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2,
                     'eseguito solo su python 2')
    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == 'Darwin',
                         'eseguito solo su macOS')
    def test_macos_only(self):
        self.assertTrue(True)

    def test_raise_skiptest(self):
        raise unittest.SkipTest('saltato tramite eccezione')
