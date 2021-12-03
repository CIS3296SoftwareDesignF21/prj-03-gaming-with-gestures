import tkinter as tk
import FingerMovement as fm
import DirectKeys as dk

def initiateFingerIdentifier():
    #fm.main()
    dk.PressKey(dk.W)

window = tk.Tk()
frame = tk.Frame()
welcome_message = tk.Label(text="Welcome. To continue, click the button below")
start_button = tk.Button(text = "Let's go!", command = initiateFingerIdentifier)

welcome_message.pack()
start_button.pack()
frame.pack()
window.mainloop()