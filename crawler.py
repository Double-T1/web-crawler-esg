from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.sustainalytics.com/esg-ratings")
all_hrefs = []
links = driver.find_elements(By.CSS_SELECTOR, "a.primary-color.d-block.js-fix-path")
hrefs = [link.get_attribute("href") for link in links]
all_hrefs += hrefs

scraped_data = []
for href in all_hrefs:
    driver.get(href)
    try:
        risk_rating_score = driver.find_element(
            By.CSS_SELECTOR, "div.col-6.risk-rating-score span"
        ).text
    except:
        continue

    try:
        company_name = driver.find_element(
            By.CSS_SELECTOR, "div.row.company-name h2"
        ).text
    except:
        company_name = "N/A"

    try:
        industry_group = driver.find_element(
            By.CSS_SELECTOR, "strong.industry-group"
        ).text
    except:
        industry_group = "N/A"

    try:
        country_or_region = driver.find_element(By.CSS_SELECTOR, "strong.country").text
    except:
        country_or_region = "N/A"

    try:
        identifier = driver.find_element(By.CSS_SELECTOR, "strong.identifier").text
    except:
        identifier = "N/A"

    try:
        risk_rating_assessment = driver.find_element(
            By.CSS_SELECTOR, "div.risk-rating-assessment span"
        ).text
    except:
        risk_rating_assessment = "N/A"

    try:
        industry_group_position = driver.find_element(
            By.CSS_SELECTOR, "strong.industry-group-position"
        ).text
    except:
        industry_group_position = "N/A"

    try:
        industry_group_positions_total = driver.find_element(
            By.CSS_SELECTOR, "span.industry-group-positions-total"
        ).text
    except:
        industry_group_positions_total = "N/A"

    try:
        universe_position = driver.find_element(
            By.CSS_SELECTOR, "strong.universe-position"
        ).text
    except:
        universe_position = "N/A"

    try:
        universe_positions_total = driver.find_element(
            By.CSS_SELECTOR, "span.universe-positions-total"
        ).text
    except:
        universe_positions_total = "N/A"

    scraped_data.append(
        {
            "Company name": company_name,
            "Industry group": industry_group,
            "Country or region": country_or_region,
            "Identifier": identifier,
            "Risk rating score": risk_rating_score,
            "Risk rating assessment": risk_rating_assessment,
            "Industry group position": industry_group_position,
            "Industry group positions total": industry_group_positions_total,
            "Universe position": universe_position,
            "Universe positions total": universe_positions_total,
        }
    )
