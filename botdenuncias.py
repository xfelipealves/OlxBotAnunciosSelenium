# Importar as bibliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o site do Anúncio

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://go.olx.com.br/grande-goiania-e-anapolis/autos-e-pecas/pecas-e-acessorios/carros-vans-e-utilitarios/4-pneus-aro-18-165-35-996223153')
time.sleep(2)

# Clicar em denunciar
driver.find_elements_by_xpath('//button[contains(@class, "pw7c9f-1 hABWtd sc-kGXeez fbFeTO")]')[2].click()
time.sleep(3)

# Entrar com a conta
driver.find_element_by_xpath('//button[contains(@class, "sc-1e2eor2-3 dKbxsH sc-kGXeez lgjpVA")]').click()
time.sleep(10)

# 