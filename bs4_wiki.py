# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:31:56 2023

@author: Liew

Requests Wikipedia main page and parse it with BeautifulSoup.

Extract the today's featured article, and did you know ... list.
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # Request a wiki webpage
    wiki_url = 'https://en.wikipedia.org/wiki/Main_Page'
    wiki_req = requests.get(wiki_url)
    print(f"{wiki_req.status_code=}")

    wiki_page = wiki_req.text
    print("Length of wiki main page is about"
          f"{len(wiki_page)/1000} thousand words.")

    # Parse with file
    # r = requests.get() contains r.content in binary format
    wiki_soup = BeautifulSoup(wiki_req.content, "lxml")
    print(f"{wiki_soup.title.string=}")

    # Navigating using tag names
    # The simplest way to navigate the parse tree is to say the name
    # of the tag you want.

    # This will find the headlines with today's featured article
    # <span class="mw-headline" id="From_today's_featured_article">
    # From today's featured article</span>
    featured_article = wiki_soup.find(
        'span', id="From_today's_featured_article")
    text = featured_article.string
    print(f"\n{text}"
          "\nOnly the first 240 characters.\n")

    # Find the text in the featured article
    tfa_list = wiki_soup.find('div', id='mp-tfa')
    tfa_p = tfa_list.find('p')
    p_text = tfa_p.get_text()
    # Take only the first 3 sentences
    sentences_list = p_text.split(". ")
    first_three_sentences = [(x+". ") for x in sentences_list[0:3]]
    print(*first_three_sentences)  # * to remove the [] in the print

    # Find the Did you know ...
    # Only print the first 3
    dyk_string = wiki_soup.find('span', id='Did_you_know_...')
    text = dyk_string.string
    print(f"\n{text}\nOnly the first 3 lists.\n")

    # Get the individual list in the article
    dyk_list = wiki_soup.find('div', id='mp-dyk')
    d_text_list = dyk_list.find_all('li')
    for i in d_text_list[0:3]:
        print(i.get_text())
