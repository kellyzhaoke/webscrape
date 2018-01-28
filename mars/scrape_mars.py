import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    #Visit website
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

#Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #create a soup object from the html 
    article= soup.find("div", class_="list_text").get_text()
    news_title=article.find("div", class_="content-title").get_text()
    news_p=article.find("div", class_="article_teaser_body").get_text()
    print(news_title)
    print(news_p)
    
    



    #listings["newstitle"] = article.find("div", class_="content-title").get_text()
    #listings["newsp"] = article.find("div", class_="article_teaser_body").get_text()
    
   

    return listings
