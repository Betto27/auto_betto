from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://netshoes.com.br/")


pesquisa = driver.find_element_by_id("search-input")

pesquisa.send_keys("modoc")

#botao_pesquisar = driver.find_element_by_css_selector(".button")

#botao_pesquisar.click()

botao_escolha = driver.find_element(By.CSS_SELECTOR, ".button")




#botao = driver.find_element_by_class_name("navbar__item")
#botao.click()



driver.maximize_window()
sleep(3)

driver.close()
