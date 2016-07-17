#!/usr/bin/env python
# -*- coding: UTF-8*-

import unittest

class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.failIf(True)

    def testError(self):
        raise RuntimeError('Errore nel test!')

if __name__ == '__main__':
    unittest.main()