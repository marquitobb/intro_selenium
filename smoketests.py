from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_test import SearchTests

assert_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assert_test])

kwargs = {
    'output': 'smoke-repot',
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)