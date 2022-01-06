import requests
import time
from plyer import notification


def hourly_checker(function):
    try:
        while True:
            function
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print(" + Check Complete\n + 1 hour to check.")
            time.sleep(1800)
            print(" + 30 minutes to check.")
            time.sleep(1800)
    except Exception as error:
        print(" - Scheduler error: " + str(error))


def domain_checker():
    domain = []
    try:
        file1 = open("D:\Gissel\dev\DomainChecker\domains.TXT", 'r')
        lines = file1.readlines()
        print(" + Lines are: " + str(lines))
    except Exception as error:
        print(" - Text file error: \n" + str(error))

    for line in lines:
        try:
            new_line = line[:-1]
            domain.append(new_line)
        except Exception as error:
            print(" - Line iteration error: \n" + str(error))

    for url in domain:
        try:
            print(" + Checking Url: " + str(url))
            result = requests.get(url)
            print(result)
            if result.status_code != 200:
                print(" ! PROBLEM WITH DOMAIN " + str(url))
            else:
                print(" + All Good")

        except Exception as error:
            print(" - Problem on Domain: " + str(url))
            print(" - Problem: " + str(error))


hourly_checker(domain_checker())
