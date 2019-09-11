from selenium import webdriver
import time
import pandas as pd

url = "https://www.imdb.com/title/tt4154796/reviews?ref_=tt_urv"

driver = webdriver.Chrome()
driver.get(url)

loadMoreButton = driver.find_element_by_xpath('//*[@id="load-more-trigger"]')
print('Load more button clicked')
loadMoreButton.click()
time.sleep(5)

dataset = pd.DataFrame(columns=[['date', 'user', 'rating', 'review']])

for i in range(1, 51):
    rating = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[1]/span/span[1]')[0]

    user = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[1]')[0]

    date = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[2]')[0]

    review = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/a')[0]

    dataset.loc[len(dataset)] = [date.text, user.text, rating.text, review.text.strip()]

dataset.to_csv('review.csv', index=False)
driver.quit()
