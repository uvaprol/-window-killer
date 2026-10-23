import psutil
import time

TARGETS = {'robloxplayerbeta.exe', 'opticraft.exe'}

while True:
    for p in psutil.process_iter(['pid', 'name']):
        try:
            name = (p.info['name'] or '').lower()
            if name in TARGETS:
                p.kill()
                print(f'Закрыт {name} (PID: {p.pid})')
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    time.sleep(1)
