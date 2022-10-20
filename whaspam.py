import pyautogui
import webbrowser


print("Introduce un numero de telefono")
num = input()

#webbrowser.open('https://wa.me/15551234567')
webbrowser.open('https://api.whatsapp.com/send?phone='+num)

pyautogui.sleep(3)

for i in range(7):
    pyautogui.press('tab')

pyautogui.press('enter')

for i in range(1):
    pyautogui.press('tab')
    
pyautogui.press('enter')