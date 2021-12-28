import requests
from datetime import datetime
import time
from plyer import notification


def domain_checker(domain):
    print("\nPlease write the domain adress to be checked\n")
    domain = []
    pre_domain = input()
    domain = pre_domain.split()
    print("domain is " + str(domain))

    try:
        for url in domain:
            print("URL is " + str(url))
            result = requests.get(url)
            print(result)
            if result.status_code == 200:
                print("All Good")
                continue
            else:
                print("PROBLEM WITH DOMAIN " + str(url))
                continue
    except Exception as error:
        print("Problem checking domain " + str(error))


domain_checker()

