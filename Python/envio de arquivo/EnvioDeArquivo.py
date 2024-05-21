import pyautogui
from time import sleep as s 
import pyperclip

# Passo 1: Entrar no navegador
pyperclip.copy("Navegador Opera GX")
pyautogui.press("win")


s(2)

pyautogui.hotkey('ctrl', 'v')

s(1)

pyautogui.press("enter")

# Passo 2: Entrar no drive e baixar o arquivo

s(3)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/u/0/my-drive")
s(1)
pyautogui.hotkey("ctrl",  "v")
s(1) 

pyautogui.press("enter")
s(5)
pyautogui.rightClick(x=346, y=310)
s(1)
pyautogui.click(x=455, y=688)
s(2)
# abrir o uaitzap
pyautogui.hotkey("ctrl", "t")
s(1)
pyperclip.copy("https://web.whatsapp.com")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
s(6)
pyautogui.click(x= 492, y-0=294)

# mandar o arquivo p kaija
pyautogui.click(x= 768, y=998)
s(2)
pyautogui.click(x=759, y=763)
s(1)
pyautogui.click(x=87, y=312)
s(0.5)
pyautogui.doubleClick(x=550, y=178)
s(0.5)
pyautogui.hotkey('enter')
s(1)
pyautogui.hotkey('alt', 'f4')
##########################################
############################################
##############################################
################################################
#################################################
##################################################