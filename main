import psutil
import pyautogui
import win32process
import threading
import pygetwindow as gw
from time import sleep



def windows_closer():
    TARGETS = {'robloxplayerbeta.exe', 'opticraft.exe'}
    while True:
        for p in psutil.process_iter(['pid', 'name']):
            try:
                name = (p.info['name'] or '').lower()
                if name in TARGETS:
                    p.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        sleep(1)

def get_window_process_name(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        return proc.name().lower()
    except Exception:
        return ""
def close_games_tabs():
    TARGET_KEYWORDS = {'игр', 'game', 'play', 'craft'}
    BROWSER_PROCESSES = {
        'chrome.exe',
        'browser.exe',
        'firefox.exe',
        'msedge.exe',
        'opera.exe',
        'amigo.exe'
    }
    try:
        while True:
            active_window = gw.getActiveWindow()
            if active_window and active_window.title:
                hwnd = active_window._hWnd
                process_name = get_window_process_name(hwnd)
                if process_name in BROWSER_PROCESSES:
                    window_title = active_window.title.lower()
                    if any(keyword in window_title for keyword in TARGET_KEYWORDS):
                        pyautogui.hotkey('ctrl', 'w')
                        sleep(1)
            sleep(0.5)
    except KeyboardInterrupt:
        print("\nМониторинг остановлен.")

if __name__ == "__main__":
    thread_closer = threading.Thread(target=windows_closer, daemon=True)
    thread_tabs = threading.Thread(target=close_games_tabs, daemon=True)

    thread_closer.start()
    thread_tabs.start()

    thread_closer.join()
    thread_tabs.join()
