import pyautogui
import webbrowser


print("Introduce un numero de telefono")
num = input()
print("¿Que mensaje quieres mandar?")
msg = input()
print("¿Cuantas veces quieres enviarlo?")
int(n = input())



#webbrowser.open('https://wa.me/15551234567')
webbrowser.open('https://api.whatsapp.com/send?phone='+num)

pyautogui.sleep(2)
pyautogui.moveTo(673,326)
pyautogui.click()

pyautogui.sleep(2)
pyautogui.moveTo(677,437)
pyautogui.click()

pyautogui.sleep(10)
pyautogui.moveTo(586,740)
pyautogui.click

for i in range(n):
    print(i)
    pyautogui.write(msg)
    pyautogui.press('enter')