"""from selenium import webdriver

class navegador:

    driver = webdriver.Chrome()
    driver.maximize_window()"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.youtube.com")

driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys("JlO")

driver.find_element_by_id("search-icon-legacy").click()

sleep(3)
res = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
print(res.text)

assert "Jennifer Lopez" in res.text


