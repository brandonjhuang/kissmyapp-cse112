import pytest
import unittest

# Delete these function placeholders
def FormatContactName(first, last):
    return ''

def IsValidContactName(first, last):
    return True

class ContactTest(unittest.TestCase):

    #--------------------------------Standard Case-----------------------------
    def test_contact_format_standard(self):
        self.assertEqual(FormatContactName('Alger', 'Vuong'), 'Alger Vuong')
        self.assertEqual(FormatContactName('Chiraag', 'Prafullchandra'), 
            'Chiraag Prafullchandra')
        self.assertEqual(FormatContactName('Jelerson', 'Zhou'), 'Jelerson Zhou')
        self.assertEqual(FormatContactName('Christopher', 'Espitia'), 
            'Christopher Espitia')

    #--------------------------------Special Cases-----------------------------

    # First name has invalid character (will filter)
    def test_contact_invalid_first(self):
        self.assertEqual(FormatContactName('-^-^-', '.CSE112.'), '--- CSE112')

    # Last name has invalid character (will filter)
    def test_contact_invalid_last(self):
        self.assertEqual(FormatContactName('Hello', '#Kiss&My&App#'),
            'Hello KissMyApp')

    # First and Last name has invalid character (will filter)
    def test_contact_invalid_first_last(self):
        self.assertEqual(FormatContactName('abc|--@-@--|cba', 'l*_*l'),
            'abc-----cba ll')

    #--------------------------------Standard----------------------------------
    def test_valid_contact_standard(self):
        # Standard first and last name
        self.assertTrue(IsValidContactName('Brandon', 'Chin'))

        # Standard first name, alphanumerical last name
        self.assertTrue(IsValidContactName('Jeffrey', 'Wang123'))

        # First name contains special character '.', standard last name
        self.assertTrue(IsValidContactName('.Timothy.', 'Pei'))

        # Both first and last name are valid special characters
        self.assertTrue(IsValidContactName('.-.', '-.-'))


    #---------------------------------Invalid----------------------------------
    # First name contains invalid characters
    def test_valid_contact_invalid_first_1(self):
        self.assertFalse(IsValidContactName('*William*', '-Quan-'))

    # First name contains invalid characters
    def test_valid_contact_invalid_first_2(self):
        self.assertFalse(IsValidContactName('$$$Brandon$$$', 'Huang'))

    # First name contains invalid special characters, last name contains 
    # valid special characters
    def test_valid_contact_invalid_first_3(self):
        self.assertFalse(IsValidContactName('<Hello>', '-World-'))

    # Last name contains invalid characters
    def test_valid_contact_invalid_last_1(self):
        self.assertFalse(IsValidContactName('Bynhan', '^Pham^%30'))

    # Last name contains invalid characters (whitespace)
    def test_valid_contact_invalid_last_2(self):
        self.assertFalse(IsValidContactName('CSE112', 'is dope'))

    # First name contains valid special characters, last name contains 
    # invalid special characters
    def test_valid_contact_invalid_last_3(self):
        self.assertFalse(IsValidContactName('...', '$=Power'))

        
    # First and last name contain invalid characters
    def test_valid_contact_invalid_first_last_1(self):
        self.assertFalse(IsValidContactName('^.^', ':D'))

    # First and last name contain invalid characters
    def test_valid_contact_invalid_first_last_2(self):
        self.assertFalse(IsValidContactName('! !', '$=Power')) 

    # First name has > 12 characters (12 char limit)
    def test_valid_contact_invalid_length_first(self):
        self.assertFalse(IsValidContactName('HiMynameIsAlgerithm', 'Vuong'))

    # Last name has > 12 characters
    def test_valid_contact_invalid_max_length_last(self):
        self.assertFalse(IsValidContactName('KissMyApp', 'IsTheBestTeam'))

    # First and Last Name have > 12 characters
    def test_valid_contact_invalid_max_length_first_last(self):
        self.assertFalse(IsValidContactName('HelloWorld2017', 'HowIsTheYearGo'))

    # First name < 1 character
    def test_valid_contact_invalid_min_length_first(self):
        self.assertFalse(IsValidContactName('', 'abc'))

    # Last name < 1 character
    def test_valid_contact_invalid_min_length_last(self):
        self.assertFalse(IsValidContactName('123abc', ''))

    # Last and First name < 1 character
    def test_valid_contact_invalid_min_length_first_last(self):
        self.assertFalse(IsValidContactName('', ''))
