# Import BeautifulSoup, lxml, requests, io, sys, and os
from bs4 import BeautifulSoup
import requests
import io
import sys
import os
import lxml

def scraper():
    print "Welcome! First, enter the website whose full list of URLs you would like to see. Then enter the specific URL you would like to scrape."

    # Specify the url
    url = raw_input("Website to view URL list for = ")

    r = requests.get("http://" + url)

    data = r.text

    soup = BeautifulSoup(data, 'lxml')

    for link in soup.find_all('a'):
        print(link.get('href'))
    
    # Now enter the specific URL you'd like to scrape
    url2 = raw_input("URL to scrape (include 'https://'!) = ")

    page = requests.get(url2)

    soup2 = BeautifulSoup(page.content, 'lxml')

    soup2.prettify()
    
    save = raw_input("Save the text file as scrape.txt? Note: this will append new content to your existing scrape file if you haven't renamed it from 'scrape.txt'. Type 'y' for yes or 'n' for no.")
    if save == "y":
            with io.open('scrape.txt', 'a', encoding='utf8') as logfile:
                logfile.write(soup2.text) 
            prompt = raw_input("Save successful! Would you like to remove script tags from your text file? Type 'y' for yes or 'n' for no.")
            if prompt == "y":
                text_output()
            if prompt == "n":
                another_file = raw_input("Would you like to scrape another file? Type 'y' for yes and 'n' for no.")
                if another_file == "y":
                    os.execl(sys.executable, sys.executable, *sys.argv)
                if another_file == "n":
                    print("Bye!")
                    exit(0)
                else:
                    print("Please enter a valid input.")
            else:
                print("Please enter a valid input.")
                os.execl(sys.executable, sys.executable, *sys.argv)
    if save == "n":
        print("Bye!")
        exit(0)
    else:
        print("Please enter a valid input.")

def text_output():
    prompt2 = raw_input("Tags removed! Would you like to save the text of the cleaned scrape as cleaned_scrape.txt? Type 'y' for yes or 'n' for no.")
    if prompt2 == "y":
        with open('scrape.txt') as s:
            soup3 = BeautifulSoup(s, 'lxml')
            [s.extract() for s in soup3('script')]
        with open('cleaned_scrape.txt', 'w') as f:
                f.write(soup3.get_text().encode('utf-8'))
        prompt3 = raw_input("Done! Start over?")
        if prompt3 == "y":
            os.execl(sys.executable, sys.executable, *sys.argv)
        if prompt3 == "n":
            print("Bye!")
            exit(0)
        else:
            print("Please enter a valid input.")
    if prompt2 == "n":
        print("Bye!")
        exit(0)
    else:
        print("Please enter a valid input.")

scraper()
text_output()
    
                
