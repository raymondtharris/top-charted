from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def getBillboardTop100():
    top100DataFrame = pd.DataFrame({'Artist':pd.Series(dtype='str'), 'Album': pd.Series(dtype='str'),'Position': pd.Series(dtype='int'),'Last Week':pd.Series(dtype='int'), 'Peak Position': pd.Series(dtype='int'), 'Weeks On Charts': pd.Series(dtype='int')})
    driver = webdriver.Chrome()
    driver.get('https://www.billboard.com/charts/hot-100/')

    chartRows = driver.find_elements(by=By.CLASS_NAME, value='o-chart-results-list-row-container')
    for row in chartRows:
        rowInfo = row.find_element(by=By.CSS_SELECTOR, value='li.lrv-u-width-100p')
        liItems = rowInfo.find_elements(by=By.TAG_NAME, value='li')
        postion = row.find_element(by=By.TAG_NAME, value='li').text
        album = liItems[0].find_element(by=By.TAG_NAME, value='h3').text
        artist = liItems[0].find_element(by=By.TAG_NAME, value='span').text
        lastWeek = liItems[3].text
        peakPosition = liItems[4].text
        weeksOnCharts = liItems[5].text
        
        chartRecord = pd.DataFrame({'Artist':artist, 'Album': album,'Position': postion,'Last Week': lastWeek, 'Peak Position': peakPosition, 'Weeks On Charts': weeksOnCharts}, index=[0])
        top100DataFrame = pd.concat([top100DataFrame, chartRecord], ignore_index=True, axis=0)

    return top100DataFrame

