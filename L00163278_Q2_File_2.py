"""
# -----------------------------
# File : L00163278_Q2_File_2.py
# Created :  27/11/2021 19:25
# Author : Rohit Mishra
# Version : v1.0.0
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : Web scraping using beautiful soup.
# -----------------------------
"""

import urllib.request
from bs4 import BeautifulSoup
import re


def read_page_contents():
    """
        read page contents method of application
        Reading of the contents of the page
        Parameters:
        Returns:
            none
    """

    url = "http://192.168.150.128/"

    request2 = urllib.request.urlopen(url)
    request = request2.read()

    return request


if __name__ == "__main__":
    '''
        Main method of application
        Web scraping using beautiful soup
        Parameters:
         none
        Returns:
         none
     '''
    html_doc = read_page_contents()  # get contents of the page.
    soup = BeautifulSoup(html_doc, 'html.parser')  # making soup from html content.
    print("This is the Main Heading of the page : ", soup.title.string)
    my_divs = soup.find_all("div", {"class": "section_header"})  # get class named, 'section_header' from soup.
    my_divs = [div.text.strip() for div in my_divs]  # get text from all section headers and strip the string.
    print("These are the heading on the page : ", my_divs)
    pattern = re.compile("[aA]pache2")  # define regex patterns to handle case.
    html_string = str(html_doc)  # convert page content to a single string.
    apache2_matches = re.findall(pattern, html_string)  # find all matches.
    print('Number of Apache2 (case insensitive) words on the page are :', len(apache2_matches))
    print('Number of paragraphs in the page are :', len(soup.findAll('p')))

