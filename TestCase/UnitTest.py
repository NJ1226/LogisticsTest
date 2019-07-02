import unittest,datetime,traceback
from BeautifulReport import BeautifulReport
import TestCase.LogisticStationManage
from TestCase.PublicMethod import Log,TestReport2


if __name__ == '__main__':
    try:
        # test_suit = unittest.TestSuite()
        # test_suit.addTest(MyTest('test1'))
        # TestReport1(test_suit)
        suit = unittest.TestLoader().loadTestsFromTestCase(TestCase.LogisticStationManage.MyTest)
        test_suit = unittest.TestSuite(suit)
        TestReport2(test_suit)
    except BaseException as e:
        message = str(e)
        message = '错误行数：' + traceback.format_exc() + message
        Log(message)
