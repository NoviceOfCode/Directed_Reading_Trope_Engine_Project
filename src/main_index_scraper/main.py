import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
from bs4.element import ResultSet

def get_index_tropes(url: str):
    lst_index_tropes = []
    lst_index_tropes_links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    index_tropes = soup.find_all('a', class_='twikilink')
    for trope in index_tropes:
        lst_index_tropes.append(trope.text)
        lst_index_tropes_links.append(trope['href'])
    return lst_index_tropes, lst_index_tropes_links
lst_index_tropes, lst_index_tropes_links = get_index_tropes('https://tvtropes.org/pmwiki/pmwiki.php/Main/Tropes')


def track_tropes_crawled(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tropes = soup.find_all('td')
    for trope in tropes:
        print(trope.text)
        print(trope['href'])
def main_page_crawler(url, lst_index_tropes_links):
    lst_tropes = []
    lst_tropes_links = []
    for link in lst_index_tropes_links:
        response = requests.get(url + link)
        soup = BeautifulSoup(response.text, 'html.parser')

track_tropes_crawled('https://tvtropes.org/pmwiki/pagelist_having_pagetype_in_namespace.php?n=Main&t=trope')
