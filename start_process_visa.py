from time import sleep
import subprocess, datetime

while True:
    d = datetime.datetime.now()
    if d.hour >= 19 or d.hour <= 3:
        subprocess.run("python visa.py")
    
    else:
        print('Aun no es horario de revisión de visas ....')

    
    sleep(30.0)
