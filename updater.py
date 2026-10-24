import sys
import subprocess
import time
import requests

CURRENT_VERSION = "1.0.0"
REPO_OWNER = "uvaprol"
REPO_NAME = "-window-killer"


def check_for_updates():
    try:
        url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/latest"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Не удалось проверить обновления.")
            return

        data = response.json()
        latest_version = data["tag_name"].strip("v")

        if latest_version > CURRENT_VERSION:
            print(f"Доступно обновление: {latest_version} (Текущая: {CURRENT_VERSION})")

            exe_asset = None
            for asset in data["assets"]:
                if asset["name"].endswith(".exe"):
                    exe_asset = asset
                    break

            if exe_asset:
                download_url = exe_asset["browser_download_url"]
                download_update(download_url)
            else:
                print("Файл .exe не найден в релизе.")
        else:
            print("У вас установлена актуальная версия.")

    except Exception as e:
        print(f"Ошибка при проверке обновлений: {e}")


def download_update(url):
    print("Скачивание обновления...")
    new_exe_path = "update_new.exe"

    response = requests.get(url, stream=True)
    with open(new_exe_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Файл скачан. Запуск процесса замены...")
    apply_update()


def apply_update():
    current_exe = sys.argv[0]
    updater_script = (
        f'timeout /t 2 /nobreak > nul && '
        f'del "{current_exe}" && '
        f'move "update_new.exe" "{current_exe}" && '
        f'start "" "{current_exe}"'
    )
    subprocess.Popen(f'cmd.exe /c {updater_script}', shell=True)
    sys.exit()

if __name__ == "__main__":
    check_for_updates()

    # Дальше идет основной код вашей программы
    print("Программа работает...")
    time.sleep(5)
