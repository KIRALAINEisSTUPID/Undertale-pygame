import subprocess
import platform

def open_terminal(command):
    system = platform.system()

    if system == "Linux":
        try:
            # Запуск команды с nohup в фоновом режиме
            subprocess.Popen(['nohup', 'kitty', '-e', 'fish', '-c', command, '&'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            subprocess.Popen(['nohup', 'gnome-terminal', '--', 'bash', '-c', command, '&'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif system == "Darwin":  # macOS
        # Используем osascript для выполнения команды без открытия окна
        subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
    elif system == "Windows":
        # Используем start для минимизации окна
        subprocess.Popen(['start', 'cmd', '/c', f"start /min {command}"], shell=True)
