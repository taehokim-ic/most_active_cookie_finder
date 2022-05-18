import unittest
import subprocess
import sys
import os 

class TestMostActiveCookie(unittest.TestCase):
      
    def test_most_active_cookie_csv_1(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.csv', '-d', '2018-12-09'], 
            capture_output=True)
        self.assertEqual(['AtY0laUfhglK3lC7'], 
                         result.stdout.decode().strip().split("\n"))
        
    def test_most_active_cookie_csv_2(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.csv', '-d', '2018-12-08'], 
            capture_output=True)
        self.assertEqual(['SAZuXPGUrfbcn5UA','4sMM2LxV07bPJzwf', \
                                    'fbcn5UAVanZf6UtG'], 
                         result.stdout.decode().strip().split("\n"))
        
    def test_most_active_cookie_csv_3(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2018-12-09'], 
            capture_output=True)
        self.assertNotEqual(['4sMM2LxV07bPJzwf'], 
                         result.stdout.decode().strip().split("\n"))  
        
    def test_most_active_cookie_txt_1(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2018-12-08'], 
            capture_output=True)
        self.assertEqual(['SAZuXPGUrfbcn5UA','4sMM2LxV07bPJzwf', \
                                    'fbcn5UAVanZf6UtG'], 
                         result.stdout.decode().strip().split("\n"))
            
    def test_most_active_cookie_txt_2(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2018-12-07'], 
            capture_output=True)
        self.assertEqual(['4sMM2LxV07bPJzwf'], 
                         result.stdout.decode().strip().split("\n"))

    def test_most_active_cookie_txt_3(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2018-12-09'], 
            capture_output=True)
        self.assertNotEqual([''], 
                         result.stdout.decode().strip().split("\n"))      

    def test_most_active_cookie_txt_wrong_param_1(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2018--07'], 
            capture_output=True)
        self.assertEqual(['Enter date in a correct format'], 
                         result.stdout.decode().strip().split("\n"))
        
    def test_most_active_cookie_txt_wrong_param_2(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.txt', '-d', '2000-22-22'], 
            capture_output=True)
        self.assertEqual(['Enter a valid date'], 
                         result.stdout.decode().strip().split("\n"))       

    def test_most_active_cookie_txt_wrong_param_3(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.csvs', '-d', '1999-'], 
            capture_output=True)
        self.assertEqual(['Enter date in a correct format'], 
                         result.stdout.decode().strip().split("\n"))
        
    def test_most_active_cookie_csv_wrong_param_1(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.csv', '-d', '2018-7'], 
            capture_output=True)
        self.assertEqual(['Enter date in a correct format'], 
                         result.stdout.decode().strip().split("\n"))
        
    def test_most_active_cookie_csv_wrong_param_2(self):
        result = subprocess.run(
            ['./most_active_cookie', 'cookie_log.csv', '-d', '2000-22-22'], 
            capture_output=True)
        self.assertEqual(['Enter a valid date'], 
                         result.stdout.decode().strip().split("\n"))       

if __name__ == '__main__':
    unittest.main()