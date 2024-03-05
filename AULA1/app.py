# PASSO A PASSO PARA COLOCAR FOTO NO PRODUTO

# PASSO 1: ENTRAR NO SISTEMA
#PASSO 2: ENTRAR NA ABA CADASTRO DE PRODUTOS
#PASSO 3: CLICAR EM PESQUISAR
#PASSO 4: PESQUISAR O PRODUTO(IGUAL AO NOME DA FOTO)
#PASSO 5:ADICIONAR A FOTO
#PASSO 6: SALVAR
#PASSO 7: REPETIR A PARTIR DO PASSO 3 ATÉ ACABAR AS FOTO


#BIBLIOTECA É UM PACOTE DE CÓDIGO QUE PERMITE FAZER ALGUMA TAREFA, SEM A NECESSIDADE DE VOCê DIGITAR OS CÓDIGOS

#BIBLIOTECA PYAUTOGUI AUTOMATIZA TELA TECLADO E MOUSE DO COMPUTADOR
# PARA IMPORTAR A BIBLIOTECA USAR IMPORT+BIBLIOTECAlogin    senha

#para importar uma base de dados, é necessário ter o pandas instalado

import pyautogui
import time
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever uma palavra
#pyautogui.press -> pressionar uma tecla
#para usar combinação de teclas: pyautogui.hotkey('ctrl','v')
#pyautogui.PAUSE faz uma pausa em cada linha do código
#time.sleep é uma pausa somente naquela parte do código
#----------------------------
pyautogui.PAUSE = 0.2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "juan@globo.com"
senha = "123ateo8"

#abrir navegador
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter")
#escrever link
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
#logar no site
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")
pyautogui.press("tab")

import pandas
tabela = pandas.read_csv("produtos.csv")


#cadastrar 1 produto
#para cada linha da tabela
for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = (str(tabela.loc[linha, "categoria"]))
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = (str(tabela.loc[linha, "custo"]))
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
    pyautogui.click(x=745, y=297)

