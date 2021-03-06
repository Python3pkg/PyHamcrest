

from hamcrest.core.core.is_ import *

import six
from hamcrest.core.core.isequal import equal_to
from hamcrest_unit_test.matcher_test import MatcherTest
from .nevermatch import NeverMatch

try:
    import unittest2 as unittest
except ImportError:
    import unittest

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

if six.PY2:
    class OldClass:
        pass

class IsTest(MatcherTest):

    def testDelegatesMatchingToNestedMatcher(self):
        self.assert_matches('should match', is_(equal_to(True)), True)
        self.assert_matches('should match', is_(equal_to(False)), False)
        self.assert_does_not_match('should not match', is_(equal_to(True)), False)
        self.assert_does_not_match('should not match', is_(equal_to(False)), True)

    def testDescriptionShouldPassThrough(self):
        self.assert_description('<True>', is_(equal_to(True)))

    def testProvidesConvenientShortcutForIsEqualTo(self):
        self.assert_matches('should match', is_('A'), 'A');
        self.assert_matches('should match', is_('B'), 'B');
        self.assert_does_not_match('should not match', is_('A'), 'B');
        self.assert_does_not_match('should not match', is_('B'), 'A');
        self.assert_description("'A'", is_('A'));

    def testProvidesConvenientShortcutForIsInstanceOf(self):
        self.assert_matches('should match', is_(str), 'A');
        self.assert_does_not_match('should not match', is_(int), 'A');

    @unittest.skipUnless(six.PY2, "Old-style classes are not relevant under Python3+")
    def testProvidesConvenientShortcutForIsInstanceOfOldStyleClass(self):
        self.assert_matches('should match', is_(OldClass), OldClass())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(is_('A'), 'A')

    def testDelegatesMismatchDescriptionToNestedMatcher(self):
        self.assert_mismatch_description(
                                NeverMatch.mismatch_description,
                                is_(NeverMatch()),
                                'hi')

    def testDelegatesDescribeMismatchToNestedMatcher(self):
        self.assert_describe_mismatch(
                                NeverMatch.mismatch_description,
                                is_(NeverMatch()),
                                'hi')


if __name__ == '__main__':
    unittest.main()
