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

    review_xpath = '//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div[1]/div[1]/div[3]/div[1]'
    expand_xpath = '//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[4]/div/div'
    if driver.find_elements_by_xpath(expand_xpath):
        review_expand_button = driver.find_elements_by_xpath(expand_xpath)[0]
        review_expand_button.click()
        print('Expand button clicked')
        review_xpath = '//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[4]/div[1]'

    rating = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[1]/span/span[1]')[0]

    user = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[1]')[0]

    date = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/div[2]/span[2]')[0]

    # review = driver.find_elements_by_xpath('//*[@id="main"]/section/div[2]/div[2]/div['+str(i)+']/div/div[1]/a')[0]

    review = driver.find_elements_by_xpath(review_xpath)[0]

    dataset.loc[len(dataset)] = [date.text, user.text, rating.text, review.text.strip()]

dataset.to_csv('data/review.csv', index=False)
driver.quit()
