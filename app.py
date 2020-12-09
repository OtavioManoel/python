from tkinter import *

menu_inicial = Tk() #inicio

menu_inicial.title("Primeiro projeto") #Muda o titulo

menu_inicial.geometry("800x450+200+200") #Define o tamanho da tela inicial & a posição

# menu_inicial.resizable(False,False) #Não permite mudar o tamanho da tela 

# menu_inicial['bg'] = 'red' # muda a cor do fundo

#botão
btn = Button(menu_inicial, text="Buscar") #Permite escutar uma função usando command(criar um evento)
btn.pack()

formulario = Entry(menu_inicial).pack()



menu_inicial.mainloop() #final