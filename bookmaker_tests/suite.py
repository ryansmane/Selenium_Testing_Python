import unittest
from main import BookmakerDashboard
from main import BookmakerLogin

dashboard_test = unittest.TestLoader().loadTestsFromTestCase(BookmakerDashboard)
login_test = unittest.TestLoader().loadTestsFromTestCase(BookmakerLogin)

test_suite = unittest.TestSuite([dashboard_test, login_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
