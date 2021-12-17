import os
a = os.popen('docker images')
b = a.read().split("\n")
column = b.pop(0)
for i in b:
    c = i.split(" ")
    while '' in c:
        c.remove('')
    try:
        print(
            f"도커 컨테이너 이름 :: {c[0]}, 도커 컨테이너 ID :: {c[2]}")
    except:
        pass
