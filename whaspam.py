import pyautogui
import webbrowser


print("Introduce un numero de telefono")
num = input()

#webbrowser.open('https://wa.me/15551234567')
webbrowser.open('https://api.whatsapp.com/send?phone='+num)

pyautogui.sleep(3)

pyautogui.moveTo(673,326)
pyautogui.click()

pyautogui.moveTo(673,326)
pyautogui.click()