import pyautogui as pag
import time

# SAI DA IDE
pag.keyDown('alt')
pag.press('tab')
pag.keyUp('alt')

for i in range(0,22):
    pag.FAILSAFE = True      

    time.sleep(2)  # Espera a janela abrir

    # SELECIONA O PDF POSTERIOR
    pag.press('down')
    # NAVEGA ATÉ O BOTÃO DE VISUALIZAR
    pag.press('tab')
    pag.press('tab')
    # ABRE O BOTÃO DE VISUALIZAR - ABRE OUTRA ABA COM O PDF
    pag.press('space')

    time.sleep(2)  # Espera o menu abrir

    # ABRE A ABA DE DOWNLOAD
    pag.keyDown('ctrl')
    pag.press('s')
    pag.keyUp('ctrl')

    time.sleep(1) # Espera a janela de download abrir

    # NAVEGA ATÉ O BOTÃO DE DOWNLOAD
    pag.press('tab')
    pag.press('tab')
    pag.press('tab')
    pag.press('space')

    time.sleep(2)  # Espera o download acabar

    # FECHA A ABA DO PDF
    pag.keyDown('ctrl')
    pag.press('w')
    pag.keyUp('ctrl')

    time.sleep(1) # Espera a aba fechar

    # NAVEGA ATÉ O BOTÃO DE SELECIONAR OUTRO PDF
    pag.keyDown('shift')
    time.sleep(0.1)   
    pag.press('tab')
    pag.press('tab')
    pag.keyUp('shift')
    