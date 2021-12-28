import requests
from datetime import datetime
import time
from plyer import notification
from apscheduler.schedulers.blocking import BlockingScheduler


def hourly_checker(function):

    scheduler = BlockingScheduler()
    scheduler.add_job(function, 'interval', hours=6)
    scheduler.start()


def domain_checker():
    domain = []
    try:
        file1 = open("D:\Gissel\dev\DomainChecker\domains.TXT", 'r')
        lines = file1.readlines()
        print("lines are: " + str(lines))
    except Exception as error:
        print("Text file error: \n" + str(error))

    for line in lines:
        try:
            new_line = line[:-1]
            domain.append(new_line)
        except Exception as error:
            print("line iteration error: \n" + str(error))

    # pre_domain = input()
    # domain = pre_domain.split()
    # print("Domains are: " + str(domain))

    for url in domain:
        try:
            print("URL is " + str(url))
            result = requests.get(url)
            print(result)
            if result.status_code != 200:
                print("PROBLEM WITH DOMAIN " + str(url))
            else:
                print("All Good")

        except Exception as error:
            print("PROBLEM WITH DOMAIN: " + str(url))
            print("Problem: " + str(error))


hourly_checker(domain_checker())

