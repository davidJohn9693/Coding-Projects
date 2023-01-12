import random, pyautogui as pyauto

for i in range(15):
    h = random.randint(0,1000)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration = 0.3)
    pyauto.hotkey("winleft", "m")