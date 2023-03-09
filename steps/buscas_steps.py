from behave import given, when, then
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

@given(u'que acesso o site do Youtube')
def step_impl(context):


    driver.get("https://www.youtube.com")

@given(u'preencho o input de pesquisa')
def step_impl(context):
    driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys("JlO")


@when(u'clico no botão de pesquisar')
def step_impl(context):

    driver.find_element_by_id("search-icon-legacy").click()


@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    assert "Jennifer Lopez" in driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").text
