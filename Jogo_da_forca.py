from tkinter import *
from Funcoes import *

class Janela:
    def __init__(self, toplevel):
        
        j.geometry("450x230")
        j.wm_iconbitmap('icone.ico')
        j.title(" Jogo da Forca")
        j.configure(background='black')


        menubar = Menu(j)
        j.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        menubar.add_cascade(label='Jogo', menu=filemenu)
        menubar.add_cascade(label='Ajuda', menu=filemenu2)

        filemenu.add_command(label='Novo Jogo', command= self.Novo_Jogo)
        filemenu.add_command(label='Sair', command=self.Quit)

        

        self.chute=""
        self.word=""
        self.palavrae = []
        self.palavra =""
        self.palavrav = []
        self.Palavra_Sorteada =""
        self.soma = 0
        self.erro = 0
        self.tentativas = []
        self.mensagem = ""
        self.space =""
        

        self.frame1 = Frame(toplevel, bg="black", colormap="new").pack()
        self.frame2 = Frame(toplevel, bg="black", colormap="new").pack()
        self.frame3 = Frame(toplevel, bg="black", colormap="new").pack()
        self.frame4 = Frame(toplevel, bg="black", colormap="new").pack()
        self.frame5 = Frame(toplevel, bg="black", colormap="new").pack()
        self.frame6 = Frame(toplevel, bg="black", colormap="new")
        self.frame6.pack(side=RIGHT)
        self.mf = Label(self.frame5, text = "")
        self.mp =Label(self.frame5, text = "")

        self.Create_Canvas()    
        self.Inicio()

    def Inicio(self):

        self.palavra = gerapalavra() 
        self.palavrav = Convert(self.palavra)
        
        for i in range(len(self.palavra)):
            self.word += "_ "
            self.palavrae.append("_")
            "A palavra é: " + self.word
        self.Palavra_Sorteada = Label(self.frame1, text=(("A palavra é: ") + self.word ) , font=("Helvetica", "16"), fg= "red", bg="black", bd = 16)
        self.Palavra_Sorteada.pack()

        self.tentativa=Entry(self.frame2,width=2,
        font=("Helvetica", "16"), bg = "Gray", fg = "black",bd="4")
        self.tentativa.focus_force() 
        self.tentativa.pack()

        self.space = Label(self.frame3, text= "aaaa", bg= "black", fg="black",font=("Helvetica", "10"))
        self.space.pack()

        self.confere=Button(self.frame4, font=("Helvetica", "10"), text='Chutar',
                            bg='pink')
        self.confere.bind("<Button-1>",self.Testar)
        self.confere.bind("<space>",self.Testar)
        self.confere.pack()

        self.mensagem = Label(self.frame5, text="" ,
                                                 font=("Helvetica", "8"), fg= "red", bg="black",bd = 10)
        self.mensagem.pack()


    def Testar(self,event):
        self.chute = self.tentativa.get().upper()
        self.tentativa.delete(0, 'end') #LIMPAR ENTRY
        self.mensagem.configure(text="")

        if self.tentativas.count(self.chute)!= 0 :
            self.mensagem.configure(text="Você já disse essa letra!")
            self.mensagem.pack()

        else:    

            for i in range(len(self.palavra)):
                if self.chute == self.palavra[i]:
                    self.palavrae.pop(i)
                    self.palavrae.insert(i,self.chute)
                    self.soma += 1
                
            if self.soma == len(self.palavra):
                self.Win()
                
            
            if self.palavrav.count(self.chute) == 0 :
                self.erro += 1
                self.Desenho()

                
                if self.erro == 8:
                    
                    self.Lose()
             
            self.word = transformastr(self.palavrae)
            self.Palavra_Sorteada.configure(text=(("A palavra é: ") + self.word ))
            self.tentativas.append(self.chute)

    def Novo_Jogo(self):
        
        self.Limpar()
        self.Create_Canvas()

        self.chute=""
        self.word=""
        self.palavrae = []
        self.palavra =""
        self.palavrav = []
        self.Palavra_Sorteada =""
        self.soma = 0
        self.erro = 0
        self.tentativas = []
        self.mensagem = ""

        

        self.palavra = gerapalavra() 
        self.palavrav = Convert(self.palavra)
        
        for i in range(len(self.palavra)):
            self.word += "_ "
            self.palavrae.append("_")
            "A palavra é: " + self.word
        self.Palavra_Sorteada = Label(self.frame1, text=(("A palavra é: ") + self.word ) , font=("Helvetica", "16"), fg= "red", bg="black", bd = 16)
        self.Palavra_Sorteada.pack()

        self.tentativa=Entry(self.frame2,width=2,
        font=("Helvetica", "16"), bg = "Gray", fg = "black",bd="4")
        self.tentativa.focus_force() 
        self.tentativa.pack()

        self.space = Label(self.frame3, text= "aaaa", bg= "black", fg="black",font=("Helvetica", "10"))
        self.space.pack()

        self.confere=Button(self.frame4, font=("Helvetica", "10"), text='Chutar',
                            bg='pink')
        self.confere.bind("<Button-1>",self.Testar)
        self.confere.bind("<space>",self.Testar)
        self.confere.pack()

        self.mensagem = Label(self.frame5, text="" ,
                                                 font=("Helvetica", "8"), fg= "red", bg="black",bd = 10)
        self.mensagem.pack()

        
    def Win(self):
        self.Limpar()
        self.mf = Label(self.frame5, text="Vitória !!!! :)" ,
                                                 font=("Arial", "45"), fg= "red", bg="black",bd = 0, anchor=CENTER)
        self.mf.pack()
        

    def Lose(self):
        self.Palavra_Sorteada.destroy()
        self.tentativa.destroy()
        self.confere.destroy()
        self.mensagem.destroy()
        self.space.destroy()
        self.mf.destroy()

        self.mf = Label(self.frame5, text="Derrota :(" ,
                                                 font=("Arial", "45"), fg= "red", bg="black",bd = 0, anchor=CENTER)
        self.mp = Label(self.frame5, text=("A palavra era:" + self.palavra),
                                                 font=("Arial", "10"), fg= "red", bg="black",bd = 0, anchor=CENTER)
        self.mf.pack()
        self.mp.pack()

    def Desenho(self):
        if self.erro == 1:
            self.canvas1.create_oval(45,65,55,80, fill="red",outline="red") # Cabeça
        elif self.erro ==2:
            self.canvas1.create_line ((50,80),(50,150), fill="red")  #Corpo
        elif self.erro ==3:
            self.canvas1.create_line(50,150,65,180, fill= "red") #perna1
        elif self.erro ==4:
            self.canvas1.create_line(50,150,35,180, fill= "red")   #perna 2
        elif self.erro ==5:
            self.canvas1.create_line(50,80,35,120, fill= "red") # braço
        elif self.erro ==6:
            self.canvas1.create_line(50,80,65,120, fill= "red") # braço
        elif self.erro ==7:
            self.canvas1.create_line(65,180,70,180, fill= "red") #pé
        elif self.erro ==8:
            self.canvas1.create_line(35,180,30,180, fill= "red") #pé
        
    def Quit(self): j.destroy()
        
    def Create_Canvas(self):
        self.canvas1 = Canvas(self.frame6, width=100, height=200,
                                            cursor='X_cursor', bg='black')
        self.canvas1.pack(side=RIGHT)
        self.canvas1.create_line ((90,20),(90,200), fill="red")#forca
        self.canvas1.create_line ((90,20),(50,20), fill="red")# forca
        self.canvas1.create_line ((50,20),(50,50), fill="red")#corda

        self.canvas1.create_oval(40, 50,60,80,fill='', outline='red') #roda

    def Limpar(self):
        self.Palavra_Sorteada.destroy()
        self.tentativa.destroy()
        self.confere.destroy()
        self.mensagem.destroy()
        self.space.destroy()
        self.canvas1.destroy()
        self.mf.destroy()
        self.mp.destroy()
    

j = Tk()
Janela(j)
j.mainloop()

