import requests
import time
import win32api
import threading


def alert(title, alert_on):
    try:
        while alert_on:
            win32api.MessageBox(0, f"{title}", 'Problem with website', 0x00001000)
            alert_on = False
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

            if result.status_code != 200:
                if result.status_code == 403:
                    print(" + All Good")
                    print("++++++++++")
                else:
                    try:
                        print(" ! PROBLEM WITH DOMAIN " + str(url))
                        t1 = threading.Thread(target=alert(url, alert_on=True))
                        t1.start()
                        print("Alert Successful")
                        t1.join()
                    except Exception as error:
                        print("Alert Error: " + str(error))
            else:
                print(" + All Good")
                print("++++++++++")

        except Exception as error:
            print(" - Problem on Domain: " + str(url))
            t1 = threading.Thread(target=alert(url, alert_on=True))
            t1.start()
            print("Alert Successful")
            t1.join()
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

if __name__ == "__main__":
    while True:
        hourly_checker(domain_checker())
