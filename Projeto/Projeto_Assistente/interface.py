# import para criar interface
from os import strerror
import pyttsx3
import requests
from tkinter import *         
from PIL import Image,ImageTk # interagir com imagens
#
import inicio
'''+++++++++++++++++++++++++++++++++++++++++++++++++++'''
comandos='''
Comandos para interagir:
Escrever= Anota tudo no bloco de 
        notas.
Exibir= Busca videos no YT.
Buscar= Busca informação da wiki.
Alarme= Definir a hora do alarme. 
Abrir = Abre sites ou softwares. 
'''

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def read_and_talk():
    text=text_info.get('1.0','end')
    
    talk(text)



def write_text(text_wiki):
    text_info.insert(INSERT,text_wiki)
    


main_window=Tk()
main_window.title("Eliza VA")

main_window.geometry("900x600")
main_window.resizable(0,0)
main_window.config(bg='#fff')


label_title=Label(main_window, text='Eliza',bg='#fff', font=('Arieal',30,'bold'))
label_title.pack(pady=10)


lee_photo=ImageTk.PhotoImage(Image.open('04_test.jpg'))
window_photo= Label(main_window,image=lee_photo,bg='#4147DD',height=420,width=300)
window_photo.pack(pady=1)

#bloco de comandos 
Canvas_comandos=Canvas(bg='#41c166',height=200,width=280)
Canvas_comandos.place(x=25,y=135)
# largura x altura
Canvas_comandos.create_text(140,90,text=comandos,fill='black', font='Arial 12 ',)


text_info=Text(main_window,bg="#41c166", fg="black")
text_info.place(x=600,y=135,height=200,width=280)
#iniciar 
button_listen= Button(main_window,text='Iniciar', fg='black',bg='#41c166',
                        font=('Arial',10, 'bold'),width=20,height=5,command=inicio.run)
button_listen.pack(pady=2)

#falar 
button_speak= Button(main_window,text='Falar', fg='black',bg='#41c166',
                         font=('Arial',15, 'bold'),command=read_and_talk)
button_speak.place(x=690,y=350, width=100,height=60)

# botão de add
button_add_files= Button(main_window,text='Adicionar', fg='black',bg='#41c166',
                        font=('Arial',15, 'bold'),command='')
button_add_files.place(x=90,y=350, width=150,height=80)


main_window.mainloop()

