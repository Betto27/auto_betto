from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/")
driver.maximize_window()

pesquisa = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
print(pesquisa)
pesquisa.clear()
pesquisa.send_keys("EMINEM")

botao = driver.find_element_by_id("search-icon-legacy")
botao.click()
sleep(3)


seleciona_video = driver.find_element_by_link_text("Eminem - Lose Yourself [HD]")
seleciona_video.click()

sleep(7)

#Clica no botão pular anuncio
pular_anuncio = driver.find_element_by_class_name("ytp-ad-skip-button-icon")
pular_anuncio.click()

#Clica no botão de tela cheia
tela_cheia = driver.find_element_by_class_name("ytp-fullscreen-button")
tela_cheia.click()

sleep(4)

#Pula para o proximo video
proximo = driver.find_element_by_class_name("ytp-next-button")
proximo.click()

sleep(4)

#Mostra as opões abaixo quando esta em tela cheia
botao_opcoes = driver.find_element_by_css_selector(".ytp-right-controls button")
botao_opcoes.click()

#Esse não funcionou
#lista_comentarios = driver.find_element_by_css_selector('#content #content-text')
#print(lista_comentarios)

sleep(40)
driver.close()


