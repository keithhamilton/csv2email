#!/usr/bin/python
# coding: utf-8

import unittest
from smtplib import SMTP, SMTPDataError

class TestCSVParse(unittest.TestCase):

    def setUp(self):
        self.tmp_csv_path='./tmp/email_file.csv'
        f = open(self.tmp_csv_path,'w')
        f.write("keith,keith.hamilton@wk.com\n")
        f.close()
        f = open(self.tmp_csv_path, 'r')
        self.csv_dummy=f.readlines()
        f.close()

        self.name_email_dictionary = {}

    def test_csv_parse(self):
        test_dictionary = {}
        test_dictionary['keith'] = 'keith.hamilton@wk.com'

        for line in self.csv_dummy:
            # split at comma
            line_split = line.split(',')
            # firstName = zero-index
            # email = first-index
            self.name_email_dictionary[line_split[0]] = line_split[1].split('\n')[0]
        
        self.assertEqual(self.name_email_dictionary, test_dictionary)

class SMTPTest(unittest.TestCase):
    def setUp(self):
        self.server = SMTP('smtp-pdx.wk.com')
        self.validEmail = 'keith.hamilton@wk.com'
        self.invalidEmail = 'keith.hamilton@'

    def test_email_is_valid(self):
        verify_code = self.server.verify(self.validEmail)
        self.assertTrue(verify_code[0] < 400)

    def test_email_not_verified(self):
        verify_code = self.server.verify(self.validEmail)
        self.assertTrue(verify_code[0] == 252)

    def test_email_not_valid(self):
        verify_code = self.server.verify(self.invalidEmail)
        self.assertTrue(verify_code[0] >= 400)

if __name__=='__main__':
    unittest.main()

