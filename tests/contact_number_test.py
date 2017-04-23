import pytest
import unittest

def FormatContactName(first, last):
    return first + ' ' + last

def IsValidContactName(first, last):
    return True

class ContactTest(unittest.TestCase):

    def test_contact_format(self):
        self.assertEqual(FormatContactName('Alger', 'Vuong'), 'Alger Vuong')
        self.assertEqual(FormatContactName('Chiraag', 'Prafullchandra'), 
            'Chiraag Prafullchandra')
        self.assertEqual(FormatContactName('Jelerson', 'Zhou'), 'Jelerson Zhou')
        self.assertEqual(FormatContactName('Christopher', 'Espitia'), 
            'Christopher Espitia')


    def test_valid_contact(self):
    #--------------------------------Success-----------------------------------
        # Standard first and last name
        self.assertTrue(IsValidContactName('Brandon', 'Chin'))

        # Standard first name, alphanumerical last name
        self.assertTrue(IsValidContactName('Jeffrey', 'Wang123'))

        # First name contains special character '.', standard last name
        self.assertTrue(IsValidContactName('.Timothy.', 'Pei'))

        # Both first and last name are valid special characters
        self.assertTrue(IsValidContactName('.-.', '-.-'))


    #---------------------------------Failure-----------------------------------
        # First name contains invalid characters
        self.assertFalse(IsValidContactName('*William*', '-Quan-'))

        # First name contains invalid characters
        self.assertFalse(IsValidContactName('$$$Brandon$$$', 'Huang'))

        # Last name contains invalid characters
        self.assertFalse(IsValidContactName('Bynhan', '^Pham^%30'))

        # First name contains alphanumeric characters 
        # Last name contains invalid characters (whitespace)
        self.assertFalse(IsValidContactName('CSE112', 'is dope'))

        # First name contains valid special characters, last name contains 
        # invalid special characters
        self.assertFalse(IsValidContactName('...', '$=Power'))

        # First name contains invalid special characters, last name contains 
        # valid special characters
        self.assertFalse(IsValidContactName('<Hello>', '-World-'))
        
        # First and last name contain invalid characters
        self.assertFalse(IsValidContactName('^.^', ':D'))

        # First and last name contain invalid characters
        self.assertFalse(IsValidContactName('! !', '$=Power')) 
