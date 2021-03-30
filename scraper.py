from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

def find():
    val = driver.find_elements_by_xpath('//*[@class="gsc_1usr"]')
    temp = [v.text.replace('\n', '##') for v in val]
    f.write('\n'.join(temp))
    return temp[-1]


def has_next_page_and_citation(last_entry):
    btn = driver.find_element_by_xpath('//*[@id="gsc_authors_bottom_pag"]/div/button[2]')
    hasNext = not btn.get_property('disabled')
    _ind = p.search(last_entry).span()
    _temp = last_entry[_ind[0]:_ind[1]].split()[-1]
    print(last_entry)
    return hasNext and (int(_temp) > 10000)


def btn_click():
    btn = driver.find_element_by_xpath('//*[@id="gsc_authors_bottom_pag"]/div/button[2]')
    btn.click()
    time.sleep(10)


if __name__ == '__main__':
    f = open('result.txt', 'a')

    driver = webdriver.Chrome('./chromedriver')
    driver.get('')
    # print('Done')
    res = []
    time.sleep(10)
    pattern = 'Cited by [0-9]+'
    p = re.compile(pattern)
    btn = driver.find_element_by_xpath('//*[@id="gsc_authors_bottom_pag"]/div/button[2]')
    last_entry = find()
    while has_next_page_and_citation(last_entry):
        btn_click()
        last_entry = find()

    f.close()