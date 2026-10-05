############################ AREA 1 - IMPORTAÇÃO
import tkinter as tk
from PIL import Image, ImageTk
import psycopg
############################ AREA 2 - FUNÇÕES

def sumirtudo():
    frame_menu.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()

def irmenu():
    sumirtudo()
    frame_menu.pack(fill="both", expand=True)

def irsala1():
    sumirtudo()
    frame_sala1.pack(fill="both", expand=True)

def irsala2():
    sumirtudo()
    frame_sala2.pack(fill="both", expand=True)

def irsala3():
    sumirtudo()
    frame_sala3.pack(fill="both", expand=True)

############################ AREA 3 - ALGORITMO
FILEIRAS = 10
COLUNAS = 20

app = tk.Tk()
app.title("Gerenciador de Cinema")
app.geometry("1000x600")
### MENU
frame_menu = tk.Frame(app)
frame_menu.pack(fill="both", expand=True)

titulo_menu = tk.Label(frame_menu, text="Gerenciador de Cinema", font=("Monocraft", 14), fg="#FF0000")
titulo_menu.place(x=395, y=30)

botao1menu = tk.Button(frame_menu, text="Ir para a sala 1", bg="#0CB63F", fg="#FFFFFF", command=irsala1)
botao1menu.place(x=500, y=100)

botao2menu = tk.Button(frame_menu, text="Ir para a sala 2", bg="#0CB63F", fg="#FFFFFF", command=irsala2)
botao2menu.place(x=500, y=130)

botao3menu = tk.Button(frame_menu, text="Ir para a sala 3", bg="#0CB63F", fg="#FFFFFF", command=irsala3)
botao3menu.place(x=500, y=160)

### SALA 1

frame_sala1 = tk.Frame(app)

titulo_sala1 = tk.Label(frame_sala1, text="Filme Atual - Minecraft", font=("Monocraft", 14))
titulo_sala1.place(x=395, y=30)

caminhoimagem = "imagens/MINECRAFT.jpg"
imagempil = Image.open(caminhoimagem)
imagemretamanhada = imagempil.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk = ImageTk.PhotoImage(imagemretamanhada)
imagem = tk.Label(frame_sala1, image=imagemtk)
imagem.place(x=450, y=60)

frame_assentos = tk.Frame(frame_sala1) #Aqui, crio um FRAME com fundo transparente
frame_assentos.place(x = 140, y = 190)   # Aqui, mando inserir o FRAME na tela.

for x in range(FILEIRAS):   # De acordo com o Excelentíssimo, Magnífico, Onisciente, Onipresente, Onipotente, Invicto, Imbatível, Indestrutível, Supremo Patriarca das Artes Marciais Místicas, Imperador Absoluto do Multiverso Conhecido, Comendador Cósmico das Forças Ocultas da Sabedoria Absoluta, Guardião dos Segredos do Tempo, Patriarca da Alquimia Mental, Protetor Supremo dos Prazos Fatais e Arquiteto de Realidades Paralelas, Mestre Sensei Doutor Roger, aqui é a parte mais difícil do código, mas isso
    letra = chr(65 + x)     # não o abala, pois sua imensa sabedoria lhe permite coisas impossíveis e inesperadas.
                            # Cada letra possui um número em uma codificação chamada ASCII, o número 65 corresponde a letra A
                            # Então, 65 + 1 seria B, 65 + 2 seria C, etc. Dessa forma, o loop vai adicionando X a 65, X sendo 
                            # O número de repetições do Loop, indo de 65 + 1, + 2, + 3, etc. E cada fila vai ganhar um número,
                            # da primeira até a última, em ordem.
    
    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"  # Aqui, montamos o código de cada cadeira. A lógica é a mesma, vou executar esse segundo for por
                                # Completo e a letra vai ser a mesma, pois ela é definida na fila. Cada fila vai ter Y colunas, 
                                # Mas a coluna é um número mesmo, para não começar em zero, adicionemos 1 a variável constante COLUNAS.

        btn = tk.Button(    # Aqui se cria um botão a cada assento criado.
            frame_assentos,
            text=codigo,
            bg='#2FA572',     # Verde
            fg='#FFFFFF'
        )
        def alternar_cor(b=btn):
                    # Alterna o estado de seleção guardado no botão
                    b.selecionado = not getattr(b, "selecionado", False)
                    
                    if b.selecionado:
                        b.config(bg="#E41515") # Vermelho quando selecionado
                    else:
                        b.config(bg="#2FA572")
        btn.config(command=alternar_cor)
        btn.grid(row=x, column=y - 1, padx=4, pady=4)   # Esse comando cria uma grade (GRID), e distribui cada elemento na posição
                                                        # X e Y, que vão fazer o loop.
botao1sala1 = tk.Button(frame_sala1, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala1.place(x=600, y=130)
botaocancelar1 = tk.Button(frame_sala1, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar1.place(x=600, y=100)
botaoreservar1 = tk.Button(frame_sala1, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar1.place(x=600, y=70)



### SALA 2

frame_sala2 = tk.Frame(app)

titulo_sala2 = tk.Label(frame_sala2, text="Filme Atual - Minecraft (Dos Criadores de IASIP)", font=("Monocraft", 14))
titulo_sala2.place(x=305, y=30)

caminhoimagem2 = "imagens/minecraftfiladelfia.jpg"
imagempil2 = Image.open(caminhoimagem2)
imagemretamanhada2 = imagempil2.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk2 = ImageTk.PhotoImage(imagemretamanhada2)
imagem2 = tk.Label(frame_sala2, image=imagemtk2)
imagem2.place(x=450, y=60)

frame_assentos2 = tk.Frame(frame_sala2) #Aqui, crio um FRAME com fundo transparente
frame_assentos2.place(x = 140, y = 190)   # Aqui, mando inserir o FRAME na tela.

for x in range(FILEIRAS):   # De acordo com o Excelentíssimo, Magnífico, Onisciente, Onipresente, Onipotente, Invicto, Imbatível, Indestrutível, Supremo Patriarca das Artes Marciais Místicas, Imperador Absoluto do Multiverso Conhecido, Comendador Cósmico das Forças Ocultas da Sabedoria Absoluta, Guardião dos Segredos do Tempo, Patriarca da Alquimia Mental, Protetor Supremo dos Prazos Fatais e Arquiteto de Realidades Paralelas, Mestre Sensei Doutor Roger, aqui é a parte mais difícil do código, mas isso
    letra = chr(65 + x)     # não o abala, pois sua imensa sabedoria lhe permite coisas impossíveis e inesperadas.
                            # Cada letra possui um número em uma codificação chamada ASCII, o número 65 corresponde a letra A
                            # Então, 65 + 1 seria B, 65 + 2 seria C, etc. Dessa forma, o loop vai adicionando X a 65, X sendo 
                            # O número de repetições do Loop, indo de 65 + 1, + 2, + 3, etc. E cada fila vai ganhar um número,
                            # da primeira até a última, em ordem.
    
    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"  # Aqui, montamos o código de cada cadeira. A lógica é a mesma, vou executar esse segundo for por
                                # Completo e a letra vai ser a mesma, pois ela é definida na fila. Cada fila vai ter Y colunas, 
                                # Mas a coluna é um número mesmo, para não começar em zero, adicionemos 1 a variável constante COLUNAS.

        btn = tk.Button(    # Aqui se cria um botão a cada assento criado.
            frame_assentos2,
            text=codigo,
            bg='#2FA572',     # Verde
            fg='#FFFFFF'
        )
        def alternar_cor(b=btn):
                    # Alterna o estado de seleção guardado no botão
                    b.selecionado = not getattr(b, "selecionado", False)
                    
                    if b.selecionado:
                        b.config(bg="#E41515") # Vermelho quando selecionado
                    else:
                        b.config(bg="#2FA572")
        btn.config(command=alternar_cor)
        btn.grid(row=x, column=y - 1, padx=4, pady=4)   # Esse comando cria uma grade (GRID), e distribui cada elemento na posição
                                                        # X e Y, que vão fazer o loop.
botao1sala2 = tk.Button(frame_sala2, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala2.place(x=600, y=130)
botaocancelar2 = tk.Button(frame_sala2, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar2.place(x=600, y=100)
botaoreservar2 = tk.Button(frame_sala2, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar2.place(x=600, y=70)

### SALA 3

frame_sala3 = tk.Frame(app)

titulo_sala3 = tk.Label(frame_sala3, text="Filme Atual - Authentic o Filme", font=("Monocraft", 14))
titulo_sala3.place(x=305, y=30)

caminhoimagem3 = "imagens/authentic.jpg"
imagempil3 = Image.open(caminhoimagem3)
imagemretamanhada3 = imagempil3.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk3 = ImageTk.PhotoImage(imagemretamanhada3)
imagem3 = tk.Label(frame_sala3, image=imagemtk3)
imagem3.place(x=450, y=60)

frame_assentos3 = tk.Frame(frame_sala3) #Aqui, crio um FRAME com fundo transparente
frame_assentos3.place(x = 140, y = 190)   # Aqui, mando inserir o FRAME na tela.

for x in range(FILEIRAS):   # De acordo com o Excelentíssimo, Magnífico, Onisciente, Onipresente, Onipotente, Invicto, Imbatível, Indestrutível, Supremo Patriarca das Artes Marciais Místicas, Imperador Absoluto do Multiverso Conhecido, Comendador Cósmico das Forças Ocultas da Sabedoria Absoluta, Guardião dos Segredos do Tempo, Patriarca da Alquimia Mental, Protetor Supremo dos Prazos Fatais e Arquiteto de Realidades Paralelas, Mestre Sensei Doutor Roger, aqui é a parte mais difícil do código, mas isso
    letra = chr(65 + x)     # não o abala, pois sua imensa sabedoria lhe permite coisas impossíveis e inesperadas.
                            # Cada letra possui um número em uma codificação chamada ASCII, o número 65 corresponde a letra A
                            # Então, 65 + 1 seria B, 65 + 2 seria C, etc. Dessa forma, o loop vai adicionando X a 65, X sendo 
                            # O número de repetições do Loop, indo de 65 + 1, + 2, + 3, etc. E cada fila vai ganhar um número,
                            # da primeira até a última, em ordem.
    
    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"  # Aqui, montamos o código de cada cadeira. A lógica é a mesma, vou executar esse segundo for por
                                # Completo e a letra vai ser a mesma, pois ela é definida na fila. Cada fila vai ter Y colunas, 
                                # Mas a coluna é um número mesmo, para não começar em zero, adicionemos 1 a variável constante COLUNAS.

        btn = tk.Button(    # Aqui se cria um botão a cada assento criado.
            frame_assentos3,
            text=codigo,
            bg='#2FA572',     # Verde
            fg='#FFFFFF'
        )
        def alternar_cor(b=btn):
            # Alterna o estado de seleção guardado no botão
            b.selecionado = not getattr(b, "selecionado", False)
            
            if b.selecionado:
                b.config(bg="#E41515") # Vermelho quando selecionado
            else:
                b.config(bg="#2FA572")
        btn.config(command=alternar_cor)
        btn.grid(row=x, column=y - 1, padx=4, pady=4)   # Esse comando cria uma grade (GRID), e distribui cada elemento na posição
                                                        # X e Y, que vão fazer o loop.
botao1sala3 = tk.Button(frame_sala3, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala3.place(x=600, y=130)
botaocancelar3 = tk.Button(frame_sala3, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar3.place(x=600, y=100)
botaoreservar3 = tk.Button(frame_sala3, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar3.place(x=600, y=70)
app.mainloop()