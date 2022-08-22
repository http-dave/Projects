"""
Names: Dave Taveras, Eleni Rotsides, Joshua Hector, Julio Lora
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Assignment: GEDCOM Project
Professor: Ens
Course: SSW 555 Agile Methods
"""

import unittest
import userStories
import datetime

# The following lists and objects are intended to be used for the parents_not_too_old tests since it takes a list of children as input
Dan = {
    "Name": "Dan",
    "Age": 14
}
Maria = {
    "Name": "Maria",
    "Age": 20
}
John = {
    "Name": "Maria",
    "Age": 5
}
Julia = {
    "Name": "Maria",
    "Age": 25
}
motherChildren = [Dan, Maria, John]
fatherChildren = [John, Julia]

# The following dictionary objects are intended to be used for US22: uniqueIds
# and US23: uniqueNameAndBirthday

dict1 = {"i1": {"Name": "John", "Birthday": "2014-04-09"},
         "i2": {"Name": "Thomas", "Birthday": "2002-09-18"},
         "i3": {"Name": "Tony", "Birthday": "2020-03-03"}}
dict2 = {"i4": {"Name": "Quincy", "Birthday": "2003-02-28"},
         "i5": {"Name": "Ashley", "Birthday": "2005-10-25"}}
dict3 = {"i6": {"Name": "Jane", "Birthday": "1997-10-05"}}

# combine to test US25: uniqueNameInFamily
dict_25 = {"i1": {"Name": "John", "Birthday": "2014-04-09"},
           "i2": {"Name": "Thomas", "Birthday": "2002-09-18"},
           "i3": {"Name": "Tony", "Birthday": "2020-03-03"},
           "i4": {"Name": "Quincy", "Birthday": "2003-02-28"},
           "i5": {"Name": "Ashley", "Birthday": "2005-10-25"},
           "i6": {"Name": "Jane", "Birthday": "1997-10-05"}}

fam_25 = {"f1": {"Children": ["i1", "i4", "i6"]},
          "f2": {"Children": ["i2", "i3"]},
          "f3": {"Children": ["i5"]}}

# Used to test US13: siblingsSpacing
dict_13 = {"i1": {"Name": "John", "Birthday": "1997-12-10"},
           "i2": {"Name": "Thomas", "Birthday": "1996-12-18"},
           "i3": {"Name": "Tony", "Birthday": "1998-06-18"},
           "i4": {"Name": "Quincy", "Birthday": "2000-02-28"},
           "i5": {"Name": "Ashley", "Birthday": "1997-8-25"},
           "i6": {"Name": "Jane", "Birthday": "1997-10-05"},
           "i7": {"Name": "Jimmy", "Birthday": "1997-10-06"}}

fam_13 = {"f1": {"Children": ["i1"]},
          "f2": {"Children": ["i2"]},
          "f3": {"Children": ["i3"]},
          "f4": {"Children": ["i4"]},
          "f5": {"Children": ["i5"]},
          "f6": {"Children": ["i6"]},
          "f7": {"Children": ["i7"]}}

#used to test US11: no_bigamy

dict_11 = {"i1": {"Death":"NA"},
         "i2": {"Death":"2000-04-01"},
         "i3": {"Death":"NA"},
         "i4": {"Death":"2010-03-03"},
         "i5": {"Death":"NA"},
         "i6": {"Death":"NA"}}

fam_11 = {"f1": {"Married":"1990-09-06","Divorced":"NA","Husband ID": "i1", "Wife ID": "i2"},
       "f2": {"Married":"2005-11-18","Divorced":"NA","Husband ID": "i4", "Wife ID": "i3"},
       "f3": {"Married":"2002","Divorced":"2011-07-08","Husband ID": "i5", "Wife ID": "i6"}}
       

# The following dictionary objects are individual and family dictionaries to be used throughout various test cases
individuals_dict = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}
families_dict = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
    'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
"""
****************************************************************
User Story 01: datesBeforeCurrent
Author: Dave Taveras
"""


class test_dateBeforeCurrent(unittest.TestCase):
    # User story 1: Dates before Current Date
    def test_dateBeforeCurrent1(self):
        result = userStories.dateBeforeCurrent("31 AUG 2000")
        self.assertTrue(result)

    def test_dateBeforeCurrent2(self):
        result = userStories.dateBeforeCurrent("9 DEC 2025")
        self.assertFalse(result)

    def test_dateBeforeCurrent3(self):
        result = userStories.dateBeforeCurrent("28 FEB 1990")
        self.assertTrue(result)

    def test_dateBeforeCurrent4(self):
        result = userStories.dateBeforeCurrent("21 FEB 2022")
        self.assertEqual(result, True)

    def test_dateBeforeCurrent5(self):
        result = userStories.dateBeforeCurrent("11 MAR 2022")
        self.assertEqual(result, True)


"""
****************************************************************
User Story 02: Birth Before Marriage
Author: Eleni Rotsides
"""


class test_birthBeforeMarriage(unittest.TestCase):
    def test_no_marriage(self):
        """Returns NA if marriage doesn't exist"""
        self.assertEqual(userStories.is_birth_before_marriage(
            "1999-8-27", "NA"), "NA")

    def test_no_birth_date(self):
        """Returns NA if birth date doesn't exist"""
        self.assertEqual(userStories.is_birth_before_marriage(
            "NA", "1999-8-27"), "NA")

    def test_birth_is_before_marriage(self):
        """Returns true if birth is before marriage"""
        self.assertEqual(userStories.is_birth_before_marriage(
            "1990-3-15", "2020-1-1"), True)

    def test_birth_is_not_before_marriage(self):
        """Returns false if birth is not before marriage"""
        self.assertAlmostEqual(userStories.is_birth_before_marriage(
            "2020-1-1", "1990-3-15"), False)

    def test_nothing_is_given(self):
        """Returns NA if both arguments are NA"""
        self.assertEqual(
            userStories.is_birth_before_marriage("NA", "NA"), "NA")


"""
****************************************************************
User Story 03: Birth Before Death
Author: Joshua Hector
"""


class test_birthBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(userStories.birth_before_death(
            datetime.date(1999, 8, 27), "NA"), "NA")

    def test_no_birth(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(userStories.birth_before_death(
            "NA", datetime.date(1999, 8, 27)), "NA")

    def test_birth_before_death(self):
        """Returns True if birth before death"""
        self.assertTrue(userStories.birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(2078, 6, 11)), True)

    def test_birth_before_death2(self):
        """Returns True if birth before death"""
        self.assertTrue(userStories.birth_before_death(
            datetime.date(2020, 12, 11), datetime.date(2020, 12, 12)), True)

    def test_death_before_birth(self):
        """Returns False if birth after death"""
        self.assertFalse(userStories.birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(1995, 6, 11)), False)


"""
****************************************************************
User Story 04: Marriage Before Divorce
Author: Dave Taveras
"""


class test_marriageBeforeDivorce(unittest.TestCase):
    def test_marriageBeforeDivorce1(self):
        result = userStories.marriageBeforeDivorce("1887-09-11", "2010-01-03")
        self.assertTrue(result)

    def test_marriageBeforeDivorce2(self):
        result = userStories.marriageBeforeDivorce("1970-08-30", "1956-07-13")
        self.assertFalse(result)

    def test_marriageBeforeDivorce3(self):
        result = userStories.marriageBeforeDivorce("1999-02-02", "1999-02-01")
        self.assertFalse(result)

    def test_marriageBeforeDivorce4(self):
        result = userStories.marriageBeforeDivorce("2005-06-04", "2008-10-09")
        self.assertTrue(result)

    def test_marriageBeforeDivorce5(self):
        result = userStories.marriageBeforeDivorce("2020-03-17", "2022-12-25")
        self.assertEqual(result, True)


"""
****************************************************************
User Story 05: Marriage Before Death
Author: Dave Taveras
"""


class test_marriageBeforeDeath(unittest.TestCase):
    def test_marriageBeforeDeath1(self):
        result = userStories.marriageBeforeDeath("2000-03-24", "2000-03-23")
        self.assertFalse(result)

    def test_marriageBeforeDeath2(self):
        result = userStories.marriageBeforeDeath("1987-05-6", "1996-09-19")
        self.assertTrue(result)

    def test_marriageBeforeDeath3(self):
        result = userStories.marriageBeforeDeath("2022-03-7", "2020-03-6")
        self.assertFalse(result)

    def test_marriageBeforeDeath4(self):
        result = userStories.marriageBeforeDeath("2005-10-25", "2005-10-26")
        self.assertEqual(result, True)

    def test_marriageBeforeDeath5(self):
        result = userStories.marriageBeforeDeath("2019-07-7", "2019-07-6")
        self.assertEqual(result, False)

    def test_marriageBeforeDeath6(self):
        self.assertRaises(
            ValueError, userStories.marriageBeforeDeath, "NA", "2000-03-23")

    def test_marriageBeforeDeath7(self):
        result = userStories.marriageBeforeDeath("1995-09-15", "NA")
        self.assertEqual(result, True)


"""
****************************************************************
User Story 06: Divorce Before Death
Author: Julio Lora
"""


class test_divorceBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns True if both spouses have not passed away"""
        self.assertEqual(userStories.is_divorce_before_death(
            "1999-08-27", "NA", "NA"), True)

    def test_divorce_before(self):
        """Returns True if the divorce happened before the death of both spouses"""
        self.assertEqual(userStories.is_divorce_before_death(
            "1999-08-27", "2005-08-27", "2010-08-27"), True)

    def test_husband_passed(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(userStories.is_divorce_before_death(
            "1999-08-27", "1999-09-27", "NA"), True)

    def test_wife_passed(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(userStories.is_divorce_before_death(
            "1999-08-27", "NA", "1999-09-27"), True)

    def test_death_before(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(userStories.is_divorce_before_death(
            "1999-08-27", "1999-05-27", "1999-04-27"), False)

    def test_bad_input(self):
        """Returns Error if divorce date is not provided"""
        self.assertRaises(ValueError, userStories.is_divorce_before_death,
                          "NA", datetime.date(1999, 8, 27), datetime.date(1999, 5, 27))


"""
****************************************************************
User Story 7: Less than 150 years old
Author: Eleni Rotsides
"""


class TestLessThan150(unittest.TestCase):
    # US07
    def test_death_less_than_150(self):
        """Returns true if death date is less than 150 years after birth date"""
        self.assertEqual(userStories.is_less_than_150(
            "1999-6-15", "NA", "2022-2-20"), True)

    def test_death_not_less_than_150(self):
        """Returns false if death date is not less than 150 years after birth date"""
        self.assertEqual(userStories.is_less_than_150(
            "1800-6-15", "NA", "2022-2-20"), False)

    def test_current_less_than_150(self):
        """Returns true if current date is less than 150 years after birth date"""
        self.assertEqual(userStories.is_less_than_150(
            "1999-6-15", "2022-2-20", "NA"), True)

    def test_current_not_less_than_150(self):
        """Returns false if current date is not less than 150 years after birth date"""
        self.assertEqual(userStories.is_less_than_150(
            "1800-6-15", "2022-2-20", "NA"), False)

    def test_nothing_is_given(self):
        """Returns NA if arguments are N/A are NA"""
        self.assertEqual(userStories.is_less_than_150(
            "NA", "NA", "NA"), "Not enough information supplied")


"""
****************************************************************
User Story 10: Marriage Before Age of 14
Author: Joshua Hector
"""


class test_marriageBefore14(unittest.TestCase):
    def test_marriage_same_date(self):
        """Returns False if the marriage is the same date as the wife and husband birth date"""
        self.assertFalse(userStories.marriage_before_14(
            datetime.date(1999, 8, 27), datetime.date(1999, 8, 27), datetime.date(1999, 8, 27)), False)

    def test_husband_birth_before_marriage(self):
        """Returns False if the husband is married before the age of 14"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2008, 8, 1), datetime.date(1999, 1, 1), datetime.date(1980, 10, 27)), False)

    def test_wife_birth_before_marriage(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2010, 6, 11), datetime.date(1990, 5, 20), datetime.date(1997, 12, 25)), False)

    def test_marriage_valid(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2015, 2, 20), datetime.date(1980, 10, 10), datetime.date(1990, 9, 27)), True)

    def test_no_marriage(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(userStories.marriage_before_14(
            "NA", datetime.date(1999, 5, 27), datetime.date(1999, 4, 27)), "NA")


"""
****************************************************************
User Story 11: No Bigamy
Author: Eleni Rotsides
"""


class test_no_bigamy(unittest.TestCase):
    def test_no_bigamy1(self):
        result = userStories.no_bigamy(fam_11, dict_11, "i1", "HUSB", "2001-07-23")
        self.assertTrue(result)

    def test_no_bigamy2(self):
        result = userStories.no_bigamy(fam_11, dict_11, "i3", "WIFE", "2009-08-01")
        self.assertFalse(result)

    def test_no_bigamy3(self):
        result = userStories.no_bigamy(fam_11, dict_11, "i5", "HUSB", "2007-01-025")
        self.assertFalse(result)


"""
****************************************************************
User Story 12: Parents are not too old
Author: Julio Lora
"""


class test_parentsNotTooOld(unittest.TestCase):
    def test_mother_too_old(self):
        """Returns False if mother is over 60 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(
            motherChildren, fatherChildren, 80, 45), False)

    def test_mother_not_too_old(self):
        """Returns True if mother is not over 60 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(
            motherChildren, fatherChildren, 50, 45), True)

    def test_father_too_old(self):
        """Returns False if father is over 80 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(
            motherChildren, fatherChildren, 45, 90), False)

    def test_father_not_too_old(self):
        """Returns True if father is not over 80 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(
            motherChildren, fatherChildren, 50, 45), True)


"""
****************************************************************
User Story 13: Siblings Spacing
Author: Dave Taveras
"""


class test_siblingsSpacing(unittest.TestCase):

    def test_siblingsSpacing1(self):
        result = userStories.siblingsSpacing("i6", "f1", dict_13, fam_13)
        self.assertFalse(result)

    def test_siblingsSpacing2(self):
        result = userStories.siblingsSpacing("i6", "f2", dict_13, fam_13)
        self.assertTrue(result)

    def test_siblingsSpacing3(self):
        result = userStories.siblingsSpacing("i6", "f3", dict_13, fam_13)
        self.assertFalse(result)

    def test_siblingsSpacing4(self):
        result = userStories.siblingsSpacing("i6", "f4", dict_13, fam_13)
        self.assertEqual(result, True)

    def test_siblingsSpacing5(self):
        result = userStories.siblingsSpacing("i6", "f5", dict_13, fam_13)
        self.assertEqual(result, False)

    def test_siblingsSpacing6(self):
        result = userStories.siblingsSpacing("i6", "f6", dict_13, fam_13)
        self.assertEqual(result, True)

    def test_siblingsSpacing7(self):
        result = userStories.siblingsSpacing("i6", "f7", dict_13, fam_13)
        self.assertEqual(result, True)


"""
****************************************************************
User Story 14: Multiple births <= 5
Author: Eleni Rotsides
"""


class TestMoreThanFiveBirths(unittest.TestCase):
    # US14
    def test_more_than_five_births(self):
        """Prints error when there are five or more siblings with the same birthday"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                       'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                       'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"},
                       'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'},
                       'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"},
                       'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'},
                       'I10': {'ID': 'NA', 'Name': 'Sally /Afton/', 'Gender': 'F', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "NA"},
                       'I11': {'ID': 'NA', 'Name': 'Mark /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "NA"}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5', 'I10', 'I11'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                    'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'},
                    'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'},
                    'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.no_more_than_5_births(individuals, families),
                         "Error: FAMILY: US14: F1: No more than five siblings should be born at the same time.\n")

    def test_less_than_five_births(self):
        """Does not print error when there are less than five siblings with the same birthday"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                       'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                       'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"},
                       'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'},
                       'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"},
                       'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                    'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'},
                    'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'},
                    'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.no_more_than_5_births(
            individuals, families), "")

    def test_more_than_five_births_diff_families(self):
        """Prints error when there are five or more siblings with the same birthday. This test will test the situation where this violation is present in more than one family"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                       'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                       'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                       'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"},
                       'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'},
                       'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"},
                       'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'},
                       'I10': {'ID': 'NA', 'Name': 'Sally /Afton/', 'Gender': 'F', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "NA"},
                       'I11': {'ID': 'NA', 'Name': 'Mark /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "NA"},
                       'I12': {'ID': 'NA', 'Name': 'Bill /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': "NA", 'Spouse': 'NA'},
                       'I13': {'ID': 'NA', 'Name': 'Bob /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': "NA", 'Spouse': 'NA'},
                       'I14': {'ID': 'NA', 'Name': 'Barley /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': "NA", 'Spouse': 'NA'},
                       'I15': {'ID': 'NA', 'Name': 'Ben /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': "NA", 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5', 'I10', 'I11'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                    'F2': {'Children': ['I1', 'I12', 'I13', 'I14', 'I15'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'},
                    'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'},
                    'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.no_more_than_5_births(individuals, families),
                         "Error: FAMILY: US14: F1: No more than five siblings should be born at the same time.\nError: FAMILY: US14: F2: No more than five siblings should be born at the same time.\n")


"""
****************************************************************
User Story 15: Fewer than 15 siblings
Author: Joshua Hector
"""


class TestFewerThan15Siblings(unittest.TestCase):
    # US15
    families_dict = {
        "family1": {
            "Children": ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16", "I17"],
            "Married": "NA"
        },
        "family2": {
            "Children": ["I1", "I2", "I3"],
            "Married": "NA"
        }
    }
    # famiies[fid] = {"Children": [], "Married": "NA", "Divorced": "NA",
    #                                  "Husband ID": "NA", "Wife ID": "NA", "Wife Name": "NA", "Husband Name": "NA"}

    def test_fewer_than_15(self):
        """Returns true if the amount of children in a family is less than 15"""
        self.assertEqual(userStories.fewer_than_15_siblings(
            TestFewerThan15Siblings.families_dict, "family2"), True)

    def test_more_than_15(self):
        """Returns false if the amount of children in a family is more than 15"""
        self.assertEqual(userStories.fewer_than_15_siblings(
            TestFewerThan15Siblings.families_dict, "family1"), False)


"""
****************************************************************
User Story 16: Male last names
Author: Eleni Rotsides
"""


class TestMaleLastNames(unittest.TestCase):
    # US16
    def test_no_husband(self):
        """Raises ValueError if there is no husband in a family"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}

        self.assertRaises(
            ValueError, userStories.male_same_last_name, individuals, families, "F2")

    def test_not_same_last_name(self):
        """Raises ValueError if male members of a family do not have the same last name"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Smith/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}

        self.assertRaises(
            ValueError, userStories.male_same_last_name, individuals, families, "F1")

    def test_same_last_name(self):
        """Returns True if all male members of a family have the same last name"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.male_same_last_name(
            individuals, families, "F1"), True)


"""
****************************************************************
User Story 17: No marriages to descendants
Author: Joshua Hector
"""


class TestNoMarriageDescendants(unittest.TestCase):
    # US17

    families_dict = {
        "family1": {
            "Children": ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16", "I17"],
            "Married": "NA",
            "Wife ID": "I20",
            "Husband ID": "I6"
        },
    }

    families_dict_true = {
        "family1": {
            "Children": ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16", "I17"],
            "Married": "NA",
            "Wife ID": "I20",
            "Husband ID": "I21"
        },
    }

    def test_no_marriage_descendants(self):
        """Returns true if there are no families that have no marriage to descendants"""
        self.assertEqual(userStories
                         .no_marriage_to_descendants(TestNoMarriageDescendants.families_dict_true), True)

    def test_marriage_descendants(self):
        """Returns false if there are families that have a marriage to descendants"""
        self.assertEqual(userStories
                         .no_marriage_to_descendants(TestNoMarriageDescendants.families_dict), False)


"""
****************************************************************
User Story 18: Siblings should not marry
Author: Eleni Rotsides
"""


class TestSiblingsNotMarried(unittest.TestCase):
    # US18
    def test_not_married_to_sibling(self):
        """Should return False if there are no siblings married to each other"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.is_siblings_married(
            individuals, families), False)

    def test_married_to_sibling(self):
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': "{'F3'}"}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': "{'F3'}"}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I5', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Gregory /Afton/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertRaises(
            ValueError, userStories.is_siblings_married, individuals, families)


"""
****************************************************************
User Story 20: Aunts and Uncles
Author: Julio Lora
"""


class test_aunts_and_uncles(unittest.TestCase):
    def test_good_marriage(self):
        """Returns False if the marriage does not include an aunt or uncle with their niece or nephew"""
        self.assertEqual(userStories.aunts_and_uncles(
            "I1", "I2", families_dict, individuals_dict), False)

    def test_bad_marriage(self):
        """Returns True if the marriage does include an aunt or uncle with their niece or nephew"""
        self.assertEqual(userStories.aunts_and_uncles(
            "I3", "I7", families_dict, individuals_dict), True)


"""
****************************************************************
User Story 21: Correct Gender Roles
Author: Julio Lora
"""


class test_correct_gender_roles(unittest.TestCase):
    def test_good_gender_roles(self):
        """Returns True if the families follow correct gender roles"""
        self.assertEqual(userStories.correct_gender_roles(
            families_dict, individuals_dict), True)

    def test_bad_gender_roles(self):
        """Returns False if the families don't follow correct gender roles"""
        self.assertEqual(userStories.correct_gender_roles(
            families_dict, individuals_dict_fake_gender_roles), False)


"""
****************************************************************
User Story 22: All ID's Are Unique
Author: Dave Taveras
"""


class test_uniqueIds(unittest.TestCase):
    def test_uniqueIds1(self):
        result = userStories.uniqueIds("i1", dict2)
        self.assertTrue(result)

    def test_uniqueIds2(self):
        result = userStories.uniqueIds("i1", dict1)
        self.assertFalse(result)

    def test_uniqueIds3(self):
        result = userStories.uniqueIds("i6", dict3)
        self.assertEqual(result, False)

    def test_uniqueIds4(self):
        result = userStories.uniqueIds("i4", dict2)
        self.assertFalse(result)

    def test_uniqueIds5(self):
        result = userStories.uniqueIds("i6", dict1)
        self.assertTrue(result)


"""
****************************************************************
User Story 23: uniqueNameAndBirthday
Author: Dave Taveras
"""


class test_uniqueNameAndBirthday(unittest.TestCase):
    def test_uniqueNameAndBirthday1(self):
        result = userStories.uniqueNameAndBirthday("John", "2014-04-09", dict1)
        self.assertEqual(result, False)

    def test_uniqueNameAndBirthday2(self):
        result = userStories.uniqueNameAndBirthday(
            "Thomas", "1987-08-05", dict1)
        self.assertEqual(result, True)

    def test_uniqueNameAndBirthday3(self):
        result = userStories.uniqueNameAndBirthday(
            "Pablo", "2020-03-03", dict1)
        self.assertEqual(result, True)

    def test_uniqueNameAndBirthday4(self):
        result = userStories.uniqueNameAndBirthday("Tony", "2020-03-03", dict1)
        self.assertEqual(result, False)

    def test_uniqueNameAndBirthday5(self):
        result = userStories.uniqueNameAndBirthday(
            "Thomas", "2002-09-18", dict1)
        self.assertEqual(result, False)


"""
****************************************************************
User Story 25: uniqueFirstNameInFamily
Author: Dave Taveras
"""


class test_uniqueFirstNameInFamily(unittest.TestCase):
    def test_uniqueFirstNameInFamily1(self):
        result = userStories.uniqueFirstNameInFamily(
            "i6", "f1", dict_25, fam_25)
        self.assertEqual(result, False)

    def test_uniqueFirstNameInFamily2(self):
        result = userStories.uniqueFirstNameInFamily(
            "i2", "f3", dict_25, fam_25)
        self.assertEqual(result, True)

    def test_uniqueFirstNameInFamily3(self):
        result = userStories.uniqueFirstNameInFamily(
            "i5", "f2", dict_25, fam_25)
        self.assertEqual(result, True)

    def test_uniqueFirstNameInFamily4(self):
        result = userStories.uniqueFirstNameInFamily(
            "i4", "f3", dict_25, fam_25)
        self.assertEqual(result, True)

    def test_uniqueFirstNameInFamily5(self):
        result = userStories.uniqueFirstNameInFamily(
            "i3", "f2", dict_25, fam_25)
        self.assertEqual(result, False)


"""
****************************************************************
User Story 29: List Deceased
Author: Julio Lora
"""


individuals_dict_no_death = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}


class test_list_deceased(unittest.TestCase):
    def test_includes_death(self):
        """Returns a list of the names of those who are deceased"""
        self.assertEqual(userStories.list_deceased(
            individuals_dict), ["Robert /Fox/"])

    def test_no_deaths(self):
        """Returns an empty list if there are no deaths"""
        self.assertEqual(userStories.list_deceased(
            individuals_dict_no_death), [])


"""
****************************************************************
User Story 30: List Living Married
Author: Julio Lora
"""


individuals_dict_living_married = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': "{'F1'}"}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': "{'F4'}"}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}

individuals_dict_no_living_married = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': "{'F1'}"}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': "{'F4'}"}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}


class test_list_living_married(unittest.TestCase):
    def test_living_married(self):
        """Returns a list of the names of those who are deceased"""
        self.assertEqual(userStories.list_living_married(individuals_dict_living_married), [
                         "William /Afton/", "Sabrina /Simmons/", "Elizabeth /Afton/", "Freddy /Fazbear/"])


# This is to be used for the test case for US21
individuals_dict_fake_gender_roles = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'F', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}


"""
****************************************************************
User Story 31: List living single
Author: Eleni Rotsides
"""


class TestListLivingSingle(unittest.TestCase):
    # US31
    def test_list_living_single(self):
        """Tests that list_living_single returns a list of all single people over the age of 30 that have never been married"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}

        self.assertEqual(userStories.list_living_single(individuals, families),
                         "William /Afton/ is over the age of 30 and has never been married.\nMichael /Afton/ is over the age of 30 and has never been married.\nElizabeth /Afton/ is over the age of 30 and has never been married.\nGregory /Afton/ is over the age of 30 and has never been married.\n")

    def test_no_single_people(self):
        """Tests that function returns nothing if there are no single people to list"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'F1'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 23, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 24, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 29, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 30, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 28, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.list_living_single(
            individuals, families), "")


"""
****************************************************************
User Story 32: List multiple births
Author: Eleni Rotsides
"""


class TestMultipleBirths(unittest.TestCase):
    # US32
    def test_multiple_births(self):
        """Tests that list_multiple_births returns a list of all people that share a birthday"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': "{'F1'}"}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': "{'F4'}"}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}

        self.assertEqual(userStories.list_multiple_births(individuals),
                         "On 2000-01-14, the following people share a birthday: William /Afton/ Sabrina /Simmons/ ")

    def test_no_multiple_births(self):
        """Tests that the function returns an empty string if there are no multiple births"""
        individuals = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}}
        families = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}, 'F2': {'Children': ['I1'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'NA', 'Wife ID': 'NA', 'Wife Name': 'NA', 'Husband Name': 'NA'}, 'F3': {
            'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}, 'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}
        self.assertEqual(userStories.male_same_last_name(
            individuals, families, "F1"), True)
        self.assertEqual(userStories.list_multiple_births(
            individuals), "")


"""
****************************************************************
User Story 33: List Orphaned Children
Author: Joshua Hector
"""


class TestOrphanedChildren(unittest.TestCase):
    # US33

    families_dict = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                     'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'},
                     'F4': {'Children': ['I9'], 'Married': '1996-10-6', 'Divorced': 'NA', 'Husband ID': 'I6', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Robert /Fox/'}}

    individuals_dict = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                        'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                        'I3': {'ID': 'I3', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                        'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                        'I5': {'ID': 'I5', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19', 'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                        'I6': {'ID': 'I6', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"},
                        'I7': {'ID': 'I7', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'},
                        'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                        'I9': {'ID': 'I9', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}
                        }

    families_dict2 = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': 'NA', 'Divorced': 'NA',
                             'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'}}

    individuals_dict2 = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                         'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                         'I3': {'ID': 'I3', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                         'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                         'I5': {'ID': 'I5', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19', 'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': '{F1}', 'Spouse': 'NA'},
                         'I6': {'ID': 'I6', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"},
                         'I7': {'ID': 'I7', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': '{F3}', 'Spouse': 'NA'},
                         'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                         'I9': {'ID': 'I9', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': '{F4}', 'Spouse': 'NA'}
                         }

    def test_orphaned_children(self):
        """Returns list of children if they are an orphan"""
        self.assertEqual(userStories
                         .orphaned_children(TestOrphanedChildren.families_dict, TestOrphanedChildren.individuals_dict), ["Montgomery /Fazbear/"])

    def test_no_orphaned_children(self):
        """Returns false if there are no children that are orphaned"""
        self.assertEqual(userStories
                         .orphaned_children(TestOrphanedChildren.families_dict2, TestOrphanedChildren.individuals_dict2), False)


"""
****************************************************************
User Story 34: List Large Age Differences
Author: Joshua Hector
"""


class TestLargeAgeDifferences(unittest.TestCase):
    # US33

    families_dict = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': '2002-01-05', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                     'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}
                     }

    individuals_dict = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                        'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                        'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                        'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                        }

    families_dict2 = {'F1': {'Children': ['I3', 'I4', 'I5'], 'Married': '2002-01-05', 'Divorced': 'NA', 'Husband ID': 'I1', 'Wife ID': 'I2', 'Wife Name': 'Sabrina /Simmons/', 'Husband Name': 'William /Afton/'},
                      'F3': {'Children': ['I7'], 'Married': '2007-08-18', 'Divorced': 'NA', 'Husband ID': 'I8', 'Wife ID': 'I4', 'Wife Name': 'Elizabeth /Afton/', 'Husband Name': 'Freddy /Fazbear/'}
                      }

    individuals_dict2 = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                         'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1980-03-4', 'Age': 42, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                         'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                         'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                         }

    def test_large_age_diff(self):
        """Returns false if there were no marriage that had a large age difference"""
        self.assertEqual(userStories
                         .large_age_diff(TestLargeAgeDifferences.families_dict, TestLargeAgeDifferences.individuals_dict), False)

    def test_no_large_age_diff(self):
        """Returns list of couples name if they had a large age difference when they were married"""
        self.assertEqual(userStories
                         .large_age_diff(TestLargeAgeDifferences.families_dict2, TestLargeAgeDifferences.individuals_dict2), ['William /Afton/', 'Sabrina /Simmons/'])


"""
****************************************************************
User Story 35: List Recent Births
Author: Joshua Hector
"""


class test_list_recent_births(unittest.TestCase):
    def test_recent_births(self):
        """Returns a list of the names of those who have been born recently"""

        individuals_dict = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '2022-04-01', 'Age': 0, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'},
                            'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '2022-03-20', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "NA"},
                            'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                            'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                            }

        self.assertEqual(userStories.recent_births(individuals_dict), [
                         "William /Afton/", "Sabrina /Simmons/"])

    def test_no_recent_births(self):
        """Returns an empty list there is nobody that was born recently"""

        individuals_dict2 = {'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                             'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                             }
        self.assertEqual(userStories.recent_births(individuals_dict2), [])


"""
****************************************************************
User Story 36: List Recent Deaths
Author: Joshua Hector
"""


class test_list_recent_births(unittest.TestCase):
    def test_recent_deaths(self):
        """Returns a list of the names of those who have died recently"""

        individuals_dict = {'I1': {'ID': 'I1', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': '{F2}', 'Spouse': 'NA'},
                            'I2': {'ID': 'I2', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"},
                            'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2022-02-10', 'Child': '{F1}', 'Spouse': 'NA'},
                            'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2022-03-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                            }

        self.assertEqual(userStories.recent_deaths(
            individuals_dict), ["Freddy /Fazbear/"])

    def test_no_recent_deaths(self):
        """Returns an empty list there is nobody that has died recently"""

        individuals_dict2 = {'I4': {'ID': 'I4', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': False, 'Death': '2012-07-24', 'Child': '{F1}', 'Spouse': 'NA'},
                             'I8': {'ID': 'I8', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': False, 'Death': '2012-07-24', 'Child': 'NA', 'Spouse': "{'F3'}"},
                             }
        self.assertEqual(userStories.recent_deaths(individuals_dict2), [])


"""
****************************************************************
User Story 42: rejectIllegitimateDates
Author: Dave Taveras
"""


class test_rejectIllegitimateDates(unittest.TestCase):
    def test_rejectIllegitimateDates1(self):
        result = userStories.rejectIllegitimateDates("2001-02-29")
        self.assertEqual(result, False)

    def test_rejectIllegitimateDates2(self):
        result = userStories.rejectIllegitimateDates("1998-12-31")
        self.assertEqual(result, True)

    def test_rejectIllegitimateDates3(self):
        result = userStories.rejectIllegitimateDates("2020-02-1")
        self.assertEqual(result, True)

    def test_rejectIllegitimateDates4(self):
        result = userStories.rejectIllegitimateDates("2015-05-35")
        self.assertEqual(result, False)

    def test_rejectIllegitimateDates5(self):
        result = userStories.rejectIllegitimateDates("1984-14-13")
        self.assertEqual(result, False)

    def test_rejectIllegitimateDates6(self):
        result = userStories.rejectIllegitimateDates("1984-09-39")
        self.assertEqual(result, False)

"""
****************************************************************
User Story 8: Birth Before Marriage of Parents
Author: Julio Lora
"""

individuals_dict_errors = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2006-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2000-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}

class test_birth_before_marriage_of_parents(unittest.TestCase):
    def test_no_errors(self):
        """Returns True if they are born after the marriage of parents and not more than 9 months after divorce"""
        self.assertEqual(userStories.birth_before_marriage_of_parents(
            families_dict, individuals_dict), True)

    def test_errors(self):
        """Returns False if they are not born after the marriage of parents and not more than 9 months after divorce"""
        self.assertEqual(userStories.birth_before_marriage_of_parents(
            families_dict, individuals_dict_errors), False)

"""
****************************************************************
User Story 9: Birth Before Death of Parents
Author: Julio Lora
"""

individuals_dict_error = {'I1': {'ID': 'NA', 'Name': 'William /Afton/', 'Gender': 'M', 'Birthday': '1943-01-1', 'Age': 79, 'Alive': True, 'Death': 'NA', 'Child': 'F2', 'Spouse': 'NA'}, 'I2': {'ID': 'NA', 'Name': 'Sabrina /Simmons/', 'Gender': 'F', 'Birthday': '1946-03-4', 'Age': 76, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F1'}"}, 'I3': {'ID': 'NA', 'Name': 'Michael /Afton/', 'Gender': 'M', 'Birthday': '1969-09-16', 'Age': 53, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I4': {'ID': 'NA', 'Name': 'Elizabeth /Afton/', 'Gender': 'F', 'Birthday': '1978-06-5', 'Age': 44, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I5': {'ID': 'NA', 'Name': 'Gregory /Afton/', 'Gender': 'M', 'Birthday': '1973-11-19',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'Age': 49, 'Alive': True, 'Death': 'NA', 'Child': 'F1', 'Spouse': 'NA'}, 'I6': {'ID': 'NA', 'Name': 'Robert /Fox/', 'Gender': 'M', 'Birthday': '1976-04-29', 'Age': 46, 'Alive': False, 'Death': '2006-07-12', 'Child': 'NA', 'Spouse': "{'F4'}"}, 'I7': {'ID': 'NA', 'Name': 'Montgomery /Fazbear/', 'Gender': 'M', 'Birthday': '2007-12-23', 'Age': 15, 'Alive': True, 'Death': 'NA', 'Child': 'F3', 'Spouse': 'NA'}, 'I8': {'ID': 'NA', 'Name': 'Freddy /Fazbear/', 'Gender': 'M', 'Birthday': '1975-03-17', 'Age': 47, 'Alive': True, 'Death': 'NA', 'Child': 'NA', 'Spouse': "{'F3'}"}, 'I9': {'ID': 'NA', 'Name': 'George /Fox/', 'Gender': 'M', 'Birthday': '2008-01-14', 'Age': 22, 'Alive': True, 'Death': 'NA', 'Child': 'F4', 'Spouse': 'NA'}}

class test_birth_before_death_of_parents(unittest.TestCase):
    def test_no_error(self):
        """Returns True if they are born before the death of the mother and within 9 months of the fathers death"""
        self.assertEqual(userStories.birth_before_death_of_parents(
            families_dict, individuals_dict), True)

    def test_error(self):
        """Returns False if they are not born before the death of the mother and within 9 months of the fathers death"""
        self.assertEqual(userStories.birth_before_death_of_parents(
            families_dict, individuals_dict_error), False)


if __name__ == '__main__':
    unittest.main()
