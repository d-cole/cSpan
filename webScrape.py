import urllib.request
import time
from trRow import trRow
from selenium import webdriver
from bs4 import BeautifulSoup

def getDate(p_text):
    start = p_text.find("Senate - ")
    end = p_text.find(")<")
    p_text = p_text[start + 9:end].replace(" ","_")
    p_text = p_text.replace(",","")
    return p_text



if __name__ == "__main__":
    url = "http://www.c-span.org/video/?325138-1/us-senate-morning-business"
    browser = webdriver.Firefox()
    browser.get(url)
    ele = browser.find_element_by_xpath('//*[@id="search-transcript"]/ul/li[1]/div/div/ul/li[2]')
    browser.execute_script("arguments[0].click()",ele)
    time.sleep(3)


    content = browser.page_source
    soup = BeautifulSoup(''.join(content))
    table = soup.findAll("table")
    tr_set = table[0].findAll("tr")

    all_tr = []
    for tr in tr_set:
        all_tr.append(trRow(tr))

    date_string = getDate(str(all_tr[0].getText().splitlines()[0]))

    


