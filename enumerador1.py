import requests
import sys
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
time.sleep(3)
sublist = open("wordlist.txt").read()
diretorios = sublist.splitlines()

for dir in diretorios:
    dir_enum = f"https://{sys.argv[1]}/{dir}"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print('diretorio valido encontrado', dir_enum)
