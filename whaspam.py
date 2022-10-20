import pyautogui
import webbrowser


print("Introduce un numero de telefono")
num = input()
print("¿Que mensaje quieres mandar?")
msg = input()


print("Introduce un numero de telefono")
num = input()

#webbrowser.open('https://wa.me/15551234567')
webbrowser.open('https://api.whatsapp.com/send?phone='+num)

pyautogui.sleep(2)
pyautogui.moveTo(673,326)
pyautogui.click()

pyautogui.sleep(2)
pyautogui.moveTo(677,437)
pyautogui.click()

pyautogui.sleep(2)
pyautogui.moveTo(586,740)
pyautogui.click

pyautogui.write()
pyautogui.press('enter')