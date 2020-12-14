import requests
import re

my_data = {"request":"true","auth_stud_id":"300034845","password":"O9IM-D21-62RE"}
site = "http://talaba.tdpu.uz/student/jadval"
r = requests.post(site, data=my_data)

print(r.text)

