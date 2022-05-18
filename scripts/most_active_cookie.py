#!/usr/bin/python3

import argparse
import sys
from not_valid_date_exception import NotValidDateException

parser = argparse.ArgumentParser(description='Process most active cookie')
parser.add_argument('file_name',
                        metavar='file_name',
                        type=str,
                        help='the name of the file')
parser.add_argument('-d',
                        type=str,
                        dest='date',
                        required=True,
                        help='UTC time format yyyy-mm-dd')

args = parser.parse_args()

file_name = args.file_name
target_date = args.date

occurrences = {}

def main():

    try:
        (t_year, t_month, t_day) = tuple(map(int, target_date.split("-")))
        
        if not date_valid(t_year, t_month, t_day):
            raise NotValidDateException
        
        with open(f'./log_files/{file_name}', 'r') as cookie_log:
            logs = iter(cookie_log.readlines())

            if file_name[-4:] == ".csv":
                next(logs, None)

            for log in list(logs):
                (cookie, time_stamp) = log.split(",")[:2]
                (date, _) = tuple(time_stamp.split(" ")[0].split("T"))
                (year, month, day) = tuple(map(int, date.split("-")))

                if (t_year, t_month, t_day) == (year, month, day):
                    if not cookie in occurrences:
                        occurrences[cookie] = 1
                    else:
                        occurrences[cookie] += 1

                if (t_year, t_month) == (year, month) and t_day > day:
                    break

        max_occurence = max(occurrences.values()) \
            if len(occurrences.values()) != 0 else 0

        max_cookies = [k for k,v in occurrences.items() if v == max_occurence]

        for cookie in max_cookies:
            print(cookie)

    except FileNotFoundError:
        print(f"File {file_name} Not Found")

    except (ValueError, TypeError):
        print("Enter date in a correct format")
        
    except NotValidDateException:
        print("Enter a valid date")

    except Exception as error:
        print(repr(error))

    sys.exit(-1)
    
def date_valid(year, month, day): 
    if year_valid(year):
        if month_valid(month):
            if day < 1:
                return False
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return day <= 31
            elif month in [4, 6, 9, 11]:
                return day <= 30
            else:
                return day <= 29 if is_leap_year(year) else day <=28 
    else:
        return False

def month_valid(month):
    return month >= 1 and month <= 12

def year_valid(year):
    return year >= 0

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    main()
