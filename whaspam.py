import pyautogui
import webbrowser


print("Introduce un numero de telefono")
num = input()

##webbrowser.open('https://wa.me/15551234567')
webbrowser.open('https://wa.me/'+num)