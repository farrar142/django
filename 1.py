# -*- coding: UTF-8 -*-
import os
import locale
import subprocess

os_encoding = locale.getpreferredencoding()
print(f"시스템 인코딩 :: {os_encoding}")
cmd = "docker ps -a"
po = subprocess.Popen(cmd, stdout=subprocess.PIPE)
decoded = po.stdout.read().decode('utf-8').strip()
tables = decoded.split("\n")
column = tables.pop(0)
if tables:
    for i in tables:
        c = i.split(" ")
        while '' in c:
            c.remove('')
        try:
            print(f"컨테이너 이름 :: {c[-1]}, 컨테이너 ID :: {c[0]},  이미지 이름 :: {c[1]}")
        except:
            pass
else:
    print("이미지 없음")
#
#
