import pyautogui as p
import subprocess
import time as t
from .limits import speak


def finish_action_console(action):
    t.sleep(0.5)
    p.write("clear")
    p.press("enter")
    p.write("echo 'Acao concluida!'")
    p.press("enter")
    speak(action)


def open_terminal():
    subprocess.run("gnome-terminal", shell=False, check=False)


def enable_airmon():
    passsudo = str(input("\nDigite a senha de usuario root-> "))
    adapter = str(input("\nDigite o adaptador-> "))
    open_terminal()
    t.sleep(1.3)
    p.write(f"sudo airmon-ng start {adapter}", interval=0.1)
    t.sleep(0.5)
    p.press("enter")
    t.sleep(0.5)
    p.write(passsudo, interval=0.1)
    p.press("enter")
    finish_action_console("Modo airmon-ng, ativado!")
