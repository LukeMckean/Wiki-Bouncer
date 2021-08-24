# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:09:50 2021

@author: 409182
"""

from bs4 import BeautifulSoup
import urllib.request
import random as r

def bouncer (wikiadd): #function input is your input, output is the list of all links on that site

    html_page = urllib.request.urlopen("http://www.wikipedia.com"+wikiadd)
    soup = BeautifulSoup(html_page, "html.parser")
    body = soup.find("div", {"id": "mw-content-text"})

    link_list = [""]*len(body.findAll('a'))
    
    for table in soup.find_all("table"): 
        table.decompose()

    
    
    for index, link in enumerate(body.findAll('a')):
        link_list[index] = link.get('href')
    
    
    link_list = list(filter(None, link_list))
    final_list = []
     
    
   # input("Yes?")
    for hype_links in link_list:
        if (("/wiki/" in hype_links) and ("File" not in hype_links) and 
            ("/wiki/Special" not in hype_links) and ("http" not in hype_links)
            and ("wiki/Help" not in hype_links) and ("Template" not in hype_links)
            and ("disambiguation" not in hype_links)):
            final_list.append(hype_links)
    final_list = list(dict.fromkeys(final_list))        
    return final_list


def replace_all(text, dic): #replaces { "/wiki/": "", "_": " "} so its more readable

    for i, j in dic.items():
        text = text.replace(i, j)
    return text




user_input = input("Input Start Article :") #User input can be replaced by random artcle

if " " in user_input: #formatting user input to wiki format
    user_input = user_input.replace(" ","_")

seed = "/wiki/"+user_input


wiki_list = bouncer(seed)    
d = { "/wiki/": "", "_": " "}


iterat = list(range(20))  #Number of times to cycle
for iterats in iterat:
    bounce = wiki_list[0]  #pull first link (0th item). For Random link replace with r.randint(0,len(wiki_lis))
    
    print (replace_all(bounce, d))
    wiki_list = bouncer(bounce)
    