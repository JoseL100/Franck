
from tkinter import font
from typing_extensions import runtime

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
import requests
from tkinter import *         #
from PIL import Image,ImageTk # interagir com imagens

# usando vosk
from vosk import Model, KaldiRecognizer
import pyaudio
from microfone import recog 


sites={
    'google':'google.com',
    'youtube':'youtube.com',
    'facebook':'facebook.com',
    'faculdade':'impacta.edu.br'
}
programas={
    'steam':r"C:\Program Files\steam\Steam.exe"


}



name='L'
microfone=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[-2].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def read_and_talk():
    text=text_info.get('1.0','end')
    talk(text)

def write_text(text_wiki):
    text_info.insert(INSERT,text_wiki)

def run():
    while True:
        rec=recog()
        print(rec)        
        if "reproduzir" in rec:#falar "falar"  depois o que voce precisa
            music=rec.replace("reproduzir",'')
            talk("Reproduzindo "+ music)# a voz da assistente
            pywhatkit.playonyt(music)#conexão com you_tube
        elif "buscar" in rec:
            buscar=rec.replace("buscar ", "")
            wikipedia.set_lang('pt')
            wiki=wikipedia.summary(buscar,2)
            write_text(buscar+": " + wiki)
            talk (wiki)
            break
        
        elif "alarme " in rec:
            num =rec.replace('alarme','')
            num=num.strip()
            talk("alarme ativara as " + num + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M')==num:
                    print("Acorda!!!")
                    mixer.init()
                    mixer.music.load("DiE4u - Bring Me The Horizon Rain Paris Cover_160k.mp3")
                    mixer.music.play()
                    if keyboard.read_key()=="s":
                        mixer.music.stop()
                        break
        elif 'abrir' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f"start opera.exe {sites[site]}",shell=True)
                    talk(f"abrindo {site}")
            for app in programas:
                if app in rec:
                    talk(f"abrir{app}")
                    os.startfile(programas[app])
        elif 'escrever' in rec:
            try:
                with open("anotações.txt","r") as f:
                    write(f)
            except FileNotFoundError as e :
                file=open("anotações.txt","w")
                write(file)
        elif "terminar" in rec:
            talk ("ATE A PROXIMA!!!")
            break
        
def write(f):
    talk("O que voce deseja escrever?")
    rec_write=recog()
    f.write(rec_write+ os.linesep)
    f.close()
    talk("tudo pronto, você pode revisar")
    sub.Popen("anotações.txt",shell=True)

        
        
            
'''+++++++++++++++++++++++++++++++++++++++++++++++++++'''
main_window=Tk()
main_window.title("lee IA")

main_window.geometry("900x600")
main_window.resizable(0,0)
main_window.config(bg='#fff')


label_title=Label(main_window, text='Assistente',bg='#fff', font=('Arieal',30,'bold'))
label_title.pack(pady=10)


lee_photo=ImageTk.PhotoImage(Image.open('03_test.jpg'))
window_photo= Label(main_window,image=lee_photo,bg='#4147DD',height=350,width=300)
window_photo.pack(pady=1)

Canvas_comandos=Canvas(bg='#3B3442',height=200,width=250)
Canvas_comandos.place(x=5,y=5)
# largura x altura
Canvas_comandos.create_text(120,75,text='jose',fill='white', font='Arial 10 ',)

text_info=Text(main_window,bg="#6dd5ed", fg="#434343")
text_info.place(x=0,y=200,height=280,width=255)

button_listen= Button(main_window,text='Escutando', fg='white',bg='#4147DD',
                        font=('Arial',10, 'bold'),width=20,height=5,command=run)
button_listen.pack(pady=10)

button_speak= Button(main_window,text='Falar', fg='white',bg='#4147DD',
                        font=('Arial',15, 'bold'),command=read_and_talk)
button_speak.place(x=625,y=190, width=100,height=30)

main_window.mainloop()

