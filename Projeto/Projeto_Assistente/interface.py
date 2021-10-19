
from tkinter import font
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import os
from pygame import mixer
import subprocess as sub
# import para criar interface
from tkinter import *         #
from PIL import Image,ImageTk # interagir com imagens

main_window=Tk()
main_window.title("lee IA")

main_window.geometry("800x400")
main_window.resizable(0,0)
main_window.config(bg='#333333')

label_title=Label(main_window, text='Lee AI',bg='#333333', font=('Arieal',30,'bold'))
label_title.pack(pady=10)


lee_photo=ImageTk.PhotoImage(Image.open('01_test.gif'))
window_photo= Label(main_window,image=lee_photo)
window_photo.pack(pady=10)

main_window.mainloop()

