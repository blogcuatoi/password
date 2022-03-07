import pyautogui
import random

keyboard = "1234567890qwertyuiopasdfghjklzxcvbnm"
keyboard_list = list(keyboard)

password = pyautogui.password("NHẬP PASSWORD: ")
guess_password = ''

while (guess_password != password):
    guess_password = random.choices(keyboard_list, k = len(password))
    print(str(guess_password))

    if (guess_password == list(password)):
        print(" mật khẩu là: "+"".join(guess_password))
        break