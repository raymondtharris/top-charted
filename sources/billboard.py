from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.billboard.com/charts/hot-100/')

chartRows = driver.find_elements(by=By.CLASS_NAME, value='o-chart-results-list-row-container')
for row in chartRows:
    rowInfo = row.find_element(by=By.CSS_SELECTOR, value='li.lrv-u-width-100p')
    liItems = rowInfo.find_elements(by=By.TAG_NAME, value='li')
    print(liItems[0].text)
    print(liItems[3].text)
    print(liItems[4].text)
    print(liItems[5].text)
    
    #for item in liItems:
    #    print(item.text)