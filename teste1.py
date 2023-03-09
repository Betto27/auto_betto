from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://blog.onedaytesting.com.br/teste-de-software/")

texto = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div/h1").text
print(texto)

texto_botao = driver.find_element_by_xpath("/html/body/main/header/section/div/div/div[2]/nav/ul/li[6]/a/span").text
print(texto_botao)

lista = driver.find_elements_by_css_selector(".entry-content p")

for i in lista:
    print(i.text)

print(lista)

sleep(4)
driver.close()