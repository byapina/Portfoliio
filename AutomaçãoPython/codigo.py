import pyautogui
import time
import pandas
#definindo o tempo de espera do programa para cada comando
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#abrindo o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# tempo de espera pois estamos trabalhando com algo que depende da internet, podendo demorar ou não para abrir
time.sleep(3)

#fazendo login
pyautogui.click(x=1895, y=410) #posição do mouse 
pyautogui.write("meu@email.com")
pyautogui.press("tab")
pyautogui.write("senha super elaborada123   11.0")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#importanto o arquivo 
tabela = pandas.read_csv("python/automação/produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=1812, y=292)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs=str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

#voltar para o início da tela
pyautogui.scroll(5000)
time.sleep(0.5)
    
    
    

