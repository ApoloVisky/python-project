#passo a passo para automação do sistema da empresa
# Passo 1> entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2> fazer login
# Passo 3> importar a base de dados do produto
#Passo 4> Cadastrar 1 produto
#Passo 5> repetir o processo para todos os produtos

import pyautogui
import time

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.hotkey -> atalho (combinação de tecla)

pyautogui.PAUSE = 0.3
#entrar no site
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
time.sleep(0.6)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep (3)
#fazer login no site

pyautogui.click(x=627, y=363)
pyautogui.write("apolo15007@gmail.com")
pyautogui.press("tab")
pyautogui.write("apolo15007")
pyautogui.press("tab")
pyautogui.press("enter")

#adicionar iten
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print (tabela)



for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    obs = tabela.loc[linha, "obs"]

   
    pyautogui.click(x=473, y=250)   
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if not pd.isna(obs):
        pyautogui.write(obs)
    
    #enviar a voltar ao topo
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(50000)


