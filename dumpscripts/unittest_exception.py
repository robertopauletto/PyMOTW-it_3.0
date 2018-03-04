# unittest_exception.py

import unittest


def raises_error(*args, **kwds):
    raise ValueError('Valore non valido: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Non rilevato ValueError')

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raises_error,
            'a',
            b='c',
        )
