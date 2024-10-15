import sqlite3

from selenium import webdriver
from selenium.webdriver.common.by import By

con = sqlite3.connect("esg.db")
sql = """
CREATE TABLE IF NOT EXISTS esg (
    id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    industry_group TEXT,
    country_or_region TEXT,
    identifier TEXT,
    risk_rating_score DECIMAL(10,2),
    risk_rating_assessment TEXT,
    industry_group_position INTEGER,
    industry_group_positions_total INTEGER,
    universe_position INTEGER,
    universe_positions_total INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""
cur = con.cursor()
cur.execute(sql)
con.close()

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
        (
            company_name,
            industry_group,
            country_or_region,
            identifier,
            risk_rating_score,
            risk_rating_assessment,
            industry_group_position,
            industry_group_positions_total,
            universe_position,
            universe_positions_total,
        )
    )


with sqlite3.connect("esg.db") as con:
    cur = con.cursor()
    for datum in scraped_data:
        sql = """
        INSERT INTO esg (
            company_name,
            industry_group,
            country_or_region,
            identifier,
            risk_rating_score,
            risk_rating_assessment,
            industry_group_position,
            industry_group_positions_total,
            universe_position,
            universe_positions_total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(sql, datum)
        con.commit()
