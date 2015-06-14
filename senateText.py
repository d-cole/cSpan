import urllib.request
import time
from trRow import trRow
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import sys


def getDate(p_text):
    """
    Parses first line of first <tr> to return formatted data
    """
    start = p_text.find("<time>")
    end = p_text.find("</time>")
    p_text = p_text[start + 6:end].replace(" ","_")
    p_text = p_text.replace(",","")
    return p_text

def writeTR(file_loc,tr,count):
    """
    Writes the transcript to a text file:
    Format:
        Date
        Speaker
        Text
    """
    output = open(file_loc+"-"+str(count)+".txt","w")
    output.write(tr.getTime() + "\n")
    output.write(tr.getSpeaker() + "\n")
    output.write(tr.getText() + "\n")
    output.close()
    return


def makeFolder(date):
    """
    Creates the folder with the given date name
    """
    if not os.path.exists(date):
        os.makedirs(date)
    return date + "/"



if __name__ == "__main__":
    #Get the url from command line argument
    url = sys.argv[1]

    #open the link in firefox
    browser = webdriver.Firefox()
    browser.get(url)

    #Change table to display Congressional Record
    ele = browser.find_element_by_xpath('//*[@id="search-transcript"]/ul/li[1]/div/div/ul/li[2]')
    browser.execute_script("arguments[0].click()",ele)

    
    #Wait for webpage to load congressional record before grabbing content
    time.sleep(10)

    #Grab content from page
    content = browser.page_source
    soup = BeautifulSoup(''.join(content))

    date_raw_text = str(soup.find("time"))
    date_string = getDate(date_raw_text)

    #Create folder from date info
    folder_dir = makeFolder(date_string)     

    #Get transcript table and break up into <tr> rows
    table = soup.findAll("table")
    tr_set = table[0].findAll("tr")

    #Create a list of trRow objects
    all_tr = []
    for tr in tr_set:
        all_tr.append(trRow(tr))

    #Write out all rows in transcript table to separate files
    # in the folder
    for i in range(0,len(all_tr)):
       writeTR(folder_dir + date_string,all_tr[i],i+1)


   
