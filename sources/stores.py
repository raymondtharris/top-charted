from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def getUrbanOutfittersBestSellers():
    bestSellersDataFrame = pd.DataFrame({'Artist':pd.Series(dtype='str'), 'Album': pd.Series(dtype='str'),'Position': pd.Series(dtype='int')})
    driver = webdriver.Chrome()
    driver.get('https://www.urbanoutfitters.com/vinyl-records?sort=tile.product.analytics.weekly.quantitySold&order=Descending')
    recordContainers = driver.find_elements(by=By.CSS_SELECTOR, value='div.c-pwa-tile-grid-inner')
    for index, record in recordContainers:
        recordInfo = record.find_element(by=By.CSS_SELECTOR, value='p.o-pwa-product-tile__heading').text
        artist, album = str.split(recordInfo, ' - ', 1)
        bestSeller = pd.DataFrame({'Artist':artist, 'Album': album,'Position': index}, index=[0])
        bestSellersDataFrame = pd.concat([bestSellersDataFrame, bestSeller], ignore_index=True, axis=0)
    return bestSellersDataFrame

driver = webdriver.Chrome()
driver.get('https://www.target.com/c/vinyl-records-music-movies-books/-/N-yz7nt?sortBy=bestselling&moveTo=product-list-grid')