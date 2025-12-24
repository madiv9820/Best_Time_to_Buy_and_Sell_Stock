import unittest
from timeout_decorator import timeout
from src.py_code.Solution import pySolution

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0)
        )
        self.__solution = pySolution()
        return super().setUp()
    
    @timeout(0.5)
    def testCase_0(self):
        prices, expectedProfit = self.__testcases[0]
        actualProfit = self.__solution.maxProfit(prices)
        self.assertEqual(expectedProfit, actualProfit)
    
    @timeout(0.5)
    def testCase_1(self):
        prices, expectedProfit = self.__testcases[1]
        actualProfit = self.__solution.maxProfit(prices)
        self.assertEqual(expectedProfit, actualProfit)

if __name__ == '__main__': unittest.main()