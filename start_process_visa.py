from time import sleep
import subprocess, datetime, os

while True:
    d = datetime.datetime.now()
    if d.hour >= 19 or d.hour <= 3:
        
        cmd = 'python3 visa.py'
        if os.name == 'nt':
            cmd = 'python visa.py'
        
        subprocess.run(cmd)
    
    elif d.hour == 3:
        print('Cerrando el proceso....')
        quit()    
    else:
        print('Aun no es horario de revisión de visas ....')

    
    sleep(30.0)
