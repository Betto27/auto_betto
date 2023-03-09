from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#driver.get("http://www.google.com")

#searchBtn = driver.find_element(By.LINK_TEXT, "Fazer login")

#webdriver.ActionChains(driver).double_click(searchBtn).perform()

#------TESTE 2 ----------------

#gmailLink = driver.find_element(By.LINK_TEXT, "Gmail")

#webdriver.ActionChains(driver).move_to_element(gmailLink).perform()

#xOffset = 100
#yOffset = 100

#webdriver.ActionChains(driver).move_by_offset(xOffset, yOffset).perform()

#-------------Teste 3-------------

driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")
# Store 'box B' as source element
targetEle  = driver.find_element(By.ID, "droppable")
# Performs drag and drop action of sourceEle onto the targetEle
webdriver.ActionChains(driver).drag_and_drop(sourceEle,targetEle).perform()