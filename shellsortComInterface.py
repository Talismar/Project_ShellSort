import random
import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image

plt.rcParams.update({'figure.max_open_warning': 0})
os.system('clear')

def gifInt():
    root = Tk()
    root.configure(bg='light blue')
    root.title('Interface Grafica com o Algoritmo de ordenação SHELL SORT')
    root.overrideredirect(False)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    file = '/home/talismar/Documents/ShellSort/OrdenandoComShellSort.gif'

    info = Image.open(file)
    frames = info.n_frames
    print(frames)

    im = [PhotoImage(
        file=file, format=f'gif -index {i}') for i in range(frames)]

    def animation(count):
        Label(text="Grafico do shell sort", font=('Arial', 20)).place(width=1800, height=57, relx=0.067)

        im2 = im[count]
        gif_label.configure(image=im2)

        count += 1
        if count == frames:
            count = 0
        root.after(300, lambda: animation(count))

    gif_label = Label(image='')
    gif_label.place(width=700, height=800, relx=0.035, relwidth=0.634, rely=0.078, relheight=0.26)

    start = Button(text='Iniciar', command=lambda: animation(0))
    start.place(width=50, height=50, relheight=0.99)

    Button(root, text="Sair", command=exit).place(width=50, height=57, relx=0.033)
    root.mainloop()

def gerarPNG(lista, contador, filename, tam, aux=-1):

    colores = ['green']

    x = np.arange(0, tam, 1)

    plt.figure(figsize=(7.52, 5))
    plt.subplots_adjust(left=0.05, bottom=0.19, right=0.98, top=0.84)
    plt.xticks(range(0, tam+1, 5))

    if aux == 0:
        plt.bar(x, lista, alpha=0.6, width=1, color='blue')
        nome = str(contador) + '.png'
        plt.savefig("/home/talismar/Documents/ShellSort/Imagens/" + nome, dpi=200)
        filename.append(imageio.imread("/home/talismar/Documents/ShellSort/Imagens/" + nome))
        return

    elif aux > 0:
        colores.clear()
        for i in range(0, tam):
            if lista[aux] == lista[i]:
                colores.append('red')
            else:
                colores.append('green')

    plt.bar(x, lista, alpha=0.5, width=1, color=colores)
    nome = str(contador) + '.png'
    plt.savefig("/home/talismar/Documents/ShellSort/Imagens/" + nome, dpi=200)
    filename.append(imageio.imread("/home/talismar/Documents/ShellSort/Imagens/" + nome))
    plt.cla()

def shellsort(lista, filename, tam):
    contador = 0
    h = len(lista) // 2

    "Gera o grafico"
    gerarPNG(lista, contador, filename, tam)

    while h > 0:
        i = h

        while i < len(lista):
            key = lista[i]
            trocou = False
            j = i - h

            while j >= 0 and lista[j] > key:
                lista[j+h] = lista[j]
                trocou = True
                j -= h

            if trocou:
                lista[j+h] = key
                contador += 1
                "Gera o grafico"
                gerarPNG(lista, contador, filename, tam, h)

            i += 1

        h = h // 2

    gerarPNG(lista, contador, filename, tam, 0)
    return lista

class Shellsort:
    def __init__(self):
        self.app = Tk()
        self.configuracao()
        self.tam = StringVar()

        Label(self.app, text='Informe o tamanho do array > ').grid(row=1, column=0, pady=10)        
        self.tamanho = Entry(self.app, textvariable=self.tam).grid(row=1, column=1)
        self.btn1 = Button(self.app, text="Seguir", command=lambda: self.chamando(self.tam.get()))
        self.btn1.grid(row=1, column=2, pady=10)

        self.app.mainloop()

    def configuracao(self):
        self.app.configure(background="#778899")
        self.app.resizable(True, True)
        self.app.geometry('475x600')
        self.app.title('Algoritmo de Ordenação')
        
        self.BoaVindas = Label(self.app, bg='#B0C4DE', text='Algoritmo de ordenação Shell-Sort', font=('Arial', 18))
        self.BoaVindas.grid(row=0, column=0, ipadx=50, columnspan=3)
        
        Label(self.app, bg='#B0C4DE', text='Vantagens:', font=('Arial', 18)).grid(row=2, column=0,  columnspan=3)
        Label(self.app, bg='#778899', text='Excelente para arquivos de tamanho moderado.', font=('Arial', 14)).grid(row=3, column=0, columnspan=3)
        Label(self.app, bg='#778899', text='Implementação é bem simples quantidade de\n código é pequena.\n', font=('Arial', 14)).grid(row=4, column=0, columnspan=3)

        Label(self.app, bg='#B0C4DE', text='Desvantagens:', font=('Arial', 18)).grid(row=5, column=0,  columnspan=3)
        Label(self.app, bg='#778899', text='O tempo de execução do algoritmo é sensível à\nordem inicial do arquivo.', font=('Arial', 14)).grid(row=6, column=0, columnspan=3)
        Label(self.app, bg='#778899', text='O método não é estável.', font=('Arial', 14)).grid(row=7, column=0, columnspan=3)

    def chamando(self, tam):
        "Array com as imagens para gerar o GIF"
        "Gerando lista aleatoria"
        self.lista = random.sample(range(int(tam)), int(tam))
        print(self.lista)

        self.algOrden(self.lista, int(tam))

    def algOrden(self, lista, tam):
        "Chamando o algoritmo de ordenação"
        self.filenames = []
        shellsort(lista, self.filenames, tam)

        "Gerando o GIF"
        imageio.mimsave("/home/talismar/Documents/ShellSort/OrdenandoComShellSort.gif", self.filenames, duration=0.2)

        print("GIF gerado com sucesso!!!")
        self.frame2 = PhotoImage(file="/home/talismar/Documents/ShellSort/OrdenandoComShellSort.gif", format="gif -index 2")
        self.app.destroy()
        quit(gifInt())

Shellsort()