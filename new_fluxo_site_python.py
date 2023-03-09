from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

#Maximiza o navegador
driver.maximize_window()

#Acessa a url inserida
driver.get("https://www.python.org/")

#localiza um elemento e clica nele
driver.find_element_by_link_text("Documentation").click()

sleep(3)

#Aciona o botao voltar da pagina
driver.back()

#Aciona o botão de avançar do navegador
driver.forward()

#Atualiza a pagina
driver.refresh()

#Obeter o titulo da página
texto = driver.title
print(texto)

#Seleciona a pagina atual do navegador
#driver.current_window_handle

# Opens a new tab and switches to new tab
#driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
#driver.switch_to.new_window('window')

driver.find_element_by_link_text("Python Docs").click()
sleep(3)
link_turorial = driver.find_element_by_link_text("Tutorial")
link_turorial.click()

captura_texto = driver.find_element_by_class_name("section").text
print(captura_texto)


sleep(4)
driver.close()