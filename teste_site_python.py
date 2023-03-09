import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Exemplo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_abrir_pagina(self):
        self.driver.get("https://www.python.org/")
        self.driver.maximize_window()

        self.pesquisa = self.driver.find_element_by_class_name("search-field")
        self.pesquisa.clear()
        self.pesquisa.send_keys("keys")
        self.pesquisa.send_keys(Keys.RETURN)

        sleep(3)

        self.botao_ir = self.driver.find_element_by_id("submit")
        self.botao_ir.click()

        sleep(3)

        self.link_chave = self.driver.find_element_by_link_text("PEP 412 -- Key-Sharing Dictionary")
        self.link_chave.click()

        sleep(3)

        self.link_referencia = self.driver.find_element_by_link_text("https://bitbucket.org/markshannon/cpython_new_dict")
        self.link_referencia.click()

        self.driver.get("https://bitbucket.org/markshannon/cpython_new_dict")

        self.res = self.driver.find_element_by_css_selector("#error h1").text
        print(self.res)
        print(self.driver.current_url)
        sleep(3)

        assert "https://bitbucket.org/markshannon/cpython_new_dict" in self.driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

