from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

url = "https://youtube.com"

driver.maximize_window()

driver.get(url)

sleep(3)


pesquisar = driver.find_element_by_name("search_query")
print(pesquisar)
pesquisar.clear()
pesquisar.send_keys("coringa")

sleep(2)
botao_pesquisar = driver.find_element_by_id("search-icon-legacy")
botao_pesquisar.click()

sleep(3)
seleciona_video = driver.find_element_by_link_text("Rap dos Coringas - CIRCO DOS HORRORES | NERD HITS")
print(seleciona_video)
seleciona_video.click()

sleep(3)
lista_comentario = driver.find_elements_by_css_selector("#video-title")
print(len(lista_comentario))
for i in lista_comentario:
    print(i.text)
    if "Rap" in i.text:
        print(f"Aqui é um dos filtros {i.text}")

sleep(5)
dentro_video = driver.find_element_by_css_selector("video")
dentro_video.click()


sleep(4)
driver.close()
