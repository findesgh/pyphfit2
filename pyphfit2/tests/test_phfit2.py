from unittest import TestCase
from ..pyphfit2 import phfit2


class Test_phfit2(TestCase):

    def test_smoke_test(self):
        """
        Make sure we can call phfit2.
        """
        phfit2(1, 1, 1, 13.6)
        return
