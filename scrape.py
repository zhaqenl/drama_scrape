#!/usr/bin/env python3
# coding: utf-8
"""

"""
from os import path, getcwd
from cfscrape import create_scraper
from bs4 import BeautifulSoup


def get_drama_day_url(drama_name):
    """Return a “Drama Day” URL (`http`-converted from `https` for `cfscrape`
    compatiblity), given an english K-Drama name (space-delimited e.g.:
    “A Piece of Your Mind”).

    Sample return value: 'http://dramaday.net/a-piece-of-your-mind'
    """
    base_url = 'http://dramaday.net/'
    converted_drama_name = '-'.join(drama_name.lower().split())
    full_url = base_url + converted_drama_name
    return full_url


def scrape(drama_day_url):
    '''Return scraped content from input `drama_day_url`.'''
    scraper = create_scraper()
    request_content = scraper.get(drama_day_url).content
    return request_content


def print_last_episode(request_content):
    '''Print last episode number from `request_contents`’s table.'''
    soup = BeautifulSoup(request_content, 'html.parser')
    episodes_table_div = soup.find('div',
                                   attrs={
                                       'class': 'supsystic-tables-wrap '
                                   })
    rows = episodes_table_div.find('tbody')
    return [r.find('td') for r in rows][-1].get_text()


if __name__ == '__main__':
    DRAMA_URL = get_drama_day_url(path.basename(getcwd()))
    REQ_CONTENT = scrape(DRAMA_URL)
    print(print_last_episode(REQ_CONTENT))
