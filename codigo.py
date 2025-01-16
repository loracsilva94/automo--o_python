#pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.click 
pyautogui.press 
pyautogui.write 

#Passo 1: Abrir o sistema da empresa
#   Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")

pyautogui.write("chorme")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

#pedir para o computador esperar 3s
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=346,y=371)
pyautogui.write("caroloracsilva@gmail.com")

pyautogui.press("tab")
pyautogui.write("minhasenhafalsa")

pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3: Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)
 
time.sleep()
#Passo 4: Cadastrar 1 produto


for linha in tabela.index:   
    pyautogui.click(x=405, y=274)#clica no 1 campo

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press ("tab")

    #marca
    tipo = tabela.loc[linha, "marca"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha,"obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter") #apertar o botao de enviar

    #numero positivo - scroll para cima
    #numero negativo - scroll para baixo
    pyautogui.scroll(10000)

#Passo 5: Repetir o passo 4 ate acabar todos os produtos

