from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
assert_equal = _test_case.assertEqual
assert_true = _test_case.assertTrue
assert_false = _test_case.assertFalse
