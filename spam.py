import pyautogui
import pyperclip
import random
import time
print("tool spam")
msg = input(">> noi dung msg: ").split(" || ")
n = int(input(">> so lan spam :"))
m = float(input(">> time delay :"))

print("starting...")
for i in range(5, 0, -1):
    print(i, end="...", flush='True')
print("start")


for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)
