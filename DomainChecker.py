import requests
import time
import win32api
import threading


def alert(title):
    try:
        win32api.MessageBox(0, f"{title}", 'Problem with website', 0x00001000)
    except Exception as error:
        print(" - Alert Error: \n - " + str(error))


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
            if result.status_code == 403:
                print(" + All Good")
            elif result.status_code != 200:
                print(" ! PROBLEM WITH DOMAIN " + str(url))
                t = threading.Thread(target=alert(url))
                t.start()
                t.join()
            else:
                print(" + All Good")

        except Exception as error:
            print(" - Problem on Domain: " + str(url))
            print(" - Problem: " + str(error))


def hourly_checker(foo):
    try:
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        foo
        print(" + Check Complete\n + 1 hour to check.")
        time.sleep(900)
        print(" + 45 minutes to check.")
        time.sleep(900)
        print(" + 30 minutes to check.")
        time.sleep(900)
        print(" + 15 minutes to check.")
        time.sleep(900)
    except Exception as error:
        print(" - Scheduler error: " + str(error))


while True:
    hourly_checker(domain_checker())
