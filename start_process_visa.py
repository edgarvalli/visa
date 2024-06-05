from time import sleep
import subprocess
import datetime
import os
import signal

pid: int = None

while True:
    d = datetime.datetime.now()
    cmd = 'python3 visa.py'

    if d.hour >= 19 or d.hour <= 3:

        if os.name == 'nt':
            cmd = 'python visa.py'

        subprocess.run(cmd)

    else:
        print('Aun no es horario de revisión de visas ....')

    sleep(30.0)
