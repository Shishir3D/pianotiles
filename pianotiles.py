import pyautogui
import time 
import keyboard
import win32api
import win32con
import tkinter as tk

def custom_click(x,y):
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def check_and_click():
    for x, y in coordinates_to_check:
        if pyautogui.pixel(x, y)[0] == 0:
            custom_click(x, y)
    root.after(100, check_and_click)

coordinates_to_check = [(844, 500), (700, 500), (600, 500), (450, 500)]

root = tk.Tk()
root.title("Not a aimbot")

start_button = tk.Button(root, text="Start Clicking", command=check_and_click)
start_button.pack()

instructions_label = tk.Label(root, text="Press 'q' to stop clicking.")
instructions_label.pack()

def stop_clicking(event):
    if event.name == 'q':
        root.quit()

keyboard.on_press(stop_clicking)

root.mainloop()