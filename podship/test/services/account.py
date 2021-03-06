#!/usr/bin/env python
#
# Copyright 2015 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

from __future__ import (absolute_import, division, print_function,
                        with_statement)

from podship.services.account import AccountService
import unittest


class AccountServiceTestCase(unittest.TestCase):
    """ Case that covers the account service.
    """

    def setUp(self):
        self.service = AccountService(self)

    def test_is_account_service(self):
        """ Dummy test that verifies if the service is an account service
        """
        # TODO: This test must go, it was designed to get travis build working
        # properly.
        self.assertEqual(self.service.__class__, AccountService)
