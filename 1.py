import os
import locale
import subprocess

os_encoding = locale.getpreferredencoding()
print("System Encdoing :: ", os_encoding)
# cmd = "docker ps -a"
# po = subprocess.Popen(cmd, stdout=subprocess.PIPE)
# decoded = po.stdout.read().decode('utf-8').strip()
logs = os.popen('docker ps -a')
tables = logs.split("\n")
column = tables.pop(0)
if tables:
    for i in tables:
        c = i.split(" ")
        while '' in c:
            c.remove('')
        try:
            print(
                "Container Name :: ", c[-1], ", Container ID :: ", c[0], ", Image Name :: ", c[1])
        except:
            pass
else:
    print("No Images")
#
#
#
