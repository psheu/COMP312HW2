'''
Created on Jun 22, 2016

@author: Student
'''
import unittest
import csv
import os

class Test(unittest.TestCase):

    with open('names.csv', 'w') as csvfile:
        fieldnames = ['school', 'zip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'school': 'Lower School', 'zip': '60660'})
        writer.writerow({'school': 'Middel School', 'zip': '90210'})
        writer.writerow({'school': 'High School', 'zip': '30080'})
    
    def test1(self):
        self.assertFalse(os.stat("names.csv").st_size == 0)
    
    def test2(self):
        zip = []
        with open('names.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                zip.append(row['zip'])   
        self.assertFalse(not zip)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()