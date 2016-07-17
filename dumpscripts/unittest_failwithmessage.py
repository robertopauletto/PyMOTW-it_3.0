#!/usr/bin/env python
# -*- coding: UTF-8*-

import unittest

class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.failIf(True, 'Il messaggio di fallimento va qui')

if __name__ == '__main__':
    unittest.main()
