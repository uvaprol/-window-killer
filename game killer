import pygetwindow as gw
import pyautogui
import time
import psutil
import win32process
def get_window_process_name(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        return proc.name().lower()
    except Exception:
        return ""
def close_games_tabs():
    TARGET_KEYWORDS = ['игр', 'game', 'play', 'craft']
    BROWSER_PROCESSES = [
        'chrome.exe',
        'browser.exe',
        'firefox.exe',
        'msedge.exe',
        'opera.exe',
        'amigo.exe'
    ]
    try:
        while True:
            active_window = gw.getActiveWindow()
            if active_window and active_window.title:
                hwnd = active_window._hWnd
                process_name = get_window_process_name(hwnd)
                if process_name in BROWSER_PROCESSES:
                    window_title = active_window.title.lower()
                    if any(keyword in window_title for keyword in TARGET_KEYWORDS):
                        print(f"[!] Закрываю вкладку браузера: '{active_window.title}' (Процесс: {process_name})")
                        pyautogui.hotkey('ctrl', 'w')
                        time.sleep(1)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nМониторинг остановлен.")

if __name__ == "__main__":
    close_games_tabs()
