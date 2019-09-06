# import requests
# from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# req = requests.get('https://www.carwale.com/marutisuzuki-cars/baleno/userreviews/')
# bs = BeautifulSoup(req.text, 'lxml')
# print(bs)

reviews = pd.DataFrame(columns=[['date', 'user_id', 'comments']])

driver = webdriver.Chrome()

for x in range(700, 706):
    driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p'+str(x))

    # for multiple comments by storing all commnet ids
    ids = driver.find_elements_by_xpath('//*[contains(@id, "Comment_")]')
    comment_ids = []
    for i in ids:
        comment_ids.append(i.get_attribute('id'))

    for x in comment_ids:
        # Extract dates
        user_date = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[2]/div[2]/span[1]/a/time')[0]
        date = user_date.get_attribute('title')

        # Extract user ids
        userid_element = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[2]/div[1]/span[1]/a[2]')[0]
        userid = userid_element.text

        # Extract Message
        user_message = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div/div[3]/div/div[1]')[0]
        comment = user_message.text

        reviews.loc[len(reviews)] = [date, userid, comment]

reviews.to_csv('reviews.csv', index=False)
driver.close()
