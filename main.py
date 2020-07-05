import pyautogui, os
from time import sleep

if __name__ == "__main__":
	pyautogui.moveTo(320, 20, 2)
	pyautogui.click()
	sleep(2)

	pyautogui.moveTo(300,87,2)
	pyautogui.click()
	pyautogui.write("https://www.facebook.com", interval=0.25)
	pyautogui.press("enter")
	sleep(3)

	pyautogui.moveTo(1055, 155)
	mail = input("Enter your email account: ")
	pyautogui.write(mail)
	pyautogui.press('tab')
	psw = input("Enter your password")
	pyautogui.write(psw)
	pyautogui.press('enter')