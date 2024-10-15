from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.sustainalytics.com/esg-ratings")
all_hrefs = []
links = driver.find_elements(By.CSS_SELECTOR, "a.primary-color.d-block.js-fix-path")
hrefs = [link.get_attribute("href") for link in links]
all_hrefs += hrefs

company_names = []
# industry group, country/region, identifier, risk rating score, risk rating assessment, industry group position, universe position,
for href in all_hrefs:
    driver.get(href)
    try:
        name = driver.find_element(By.CSS_SELECTOR, "div.row.company-name h2").text
    except:
        name = "Not Found"
    company_names.append(name)
