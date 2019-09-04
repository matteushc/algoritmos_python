from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = Options()

chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)

#url = "https://news.ycombinator.com/"

url = "http://www.portaltransparencia.gov.br/"
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sobre o Portal']")))

driver.find_element_by_xpath(u'//a[text()="Sobre o Portal"]').click()

driver.find_element_by_xpath(u'//a[text()="Dados do portal"]').click()
driver.find_element_by_xpath(u'//a[text()="Dados abertos"]').click()

time.sleep(5)

button_col = driver.find_elements_by_xpath("//button[@data-target='#collapse-1']")
button_col[0].click()


wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Execução da despesa']")))
driver.find_element_by_xpath(u'//a[text()="Execução da despesa"]').click()


btn_download = driver.find_elements_by_id("btn")
btn_download[0].click()

