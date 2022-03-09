# Importar as bibliotecas

from webbrowser import Chrome
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www2.olx.com.br/desapega')
time.sleep(15)

def publicar_Olx():
    # Navegar até a Olx
    
    driver.get('https://www2.olx.com.br/desapega')
    time.sleep(2)

    # Mensagem

    titulo = 'AnuncioZin'
    descricao = 'numero tal'
    cep = '74672010'

    # Preencher dados
    dados = driver.find_element_by_xpath(
            '//input[contains(@id, "input_subject")]')
    time.sleep(1)
    dados.click()
    dados.send_keys(titulo)

    dados = driver.find_element_by_xpath(
            '//textarea[contains(@id, "input_body")]')
    time.sleep(1)
    dados.click()
    dados.send_keys(descricao)

    # Escolher categoria de Serviços
    driver.find_element_by_xpath(
        '//a[contains(@id, "category_item-7060")]').click()
    time.sleep(1)

    # Selecionar tipos

    tipos = driver.find_elements_by_xpath(
        '//input[contains(@id, "service_type")]')
    tipos[0].send_keys(Keys.SPACE)
    time.sleep(0.1)
    tipos[1].send_keys(Keys.SPACE)
    time.sleep(0.1)
    tipos[3].send_keys(Keys.SPACE)
    time.sleep(0.1)
    tipos[4].send_keys(Keys.SPACE)
    time.sleep(0.1)
    tipos[8].send_keys(Keys.SPACE)
    time.sleep(0.1)
    tipos[9].send_keys(Keys.SPACE)
    time.sleep(1)

    # Colocar CEP

    endereco = driver.find_element_by_xpath(
        '//input[contains(@name, "zipcode")]')
    time.sleep(2)
    endereco.click()
    endereco.send_keys(Keys.CONTROL + "a")
    endereco.send_keys(Keys.DELETE)
    endereco.send_keys(cep)
    time.sleep(2)


    # Colocar Foto
    foto = driver.find_element_by_xpath(
        '//span[contains(@class, "isvg loaded box__icon")]')
    foto.click()
    time.sleep(2)

    foto = driver.find_element_by_xpath(
        '//input[contains(@class, "box__field")]')
    foto.send_keys(os.getcwd()+"\\arquivos\\image.jpg")
    #pyautogui.typewrite("eae galera", interval=0.30)
    pyautogui.press('esc')

    time.sleep(3)

    # Clicar em Enviar anuncio

    driver.find_element_by_xpath(
        '//button[contains(@id, "ad_insertion_submit_button")]').click()

    time.sleep(5)

driver.find_element_by_id("cookie-notice-ok-button").click()

for i in range(3):
    publicar_Olx()