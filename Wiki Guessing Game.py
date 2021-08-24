
"""
Created on Thu Aug 19 14:09:50 2021

@author: 409182
"""

from bs4 import BeautifulSoup
import urllib.request
import random as r

my_file = open("animals.txt", "r")
animals_str = my_file.read()
animals = animals_str.split('\n')


    
def bouncer (wikiadd):
    try:
        html_page = urllib.request.urlopen("http://www.wikipedia.com"+wikiadd)
        
        soup = BeautifulSoup(html_page, "html.parser")
        body = soup.find("div", {"id": "mw-content-text"})
        
        for div in soup.find_all("div", {'class':'navbox'}): 
            div.decompose()
            
        for div in soup.find_all("id", {'id':'References'}): 
            div.decompose()
        for table in soup.find_all("table"): 
            table.decompose()
     
        
        
        link_list = [""]*len(body.findAll('a'))
        
        for index, link in enumerate(body.findAll('a')):
            link_list[index] = link.get('href')
        
        
        link_list = list(filter(None, link_list))
        final_list = []
   
        #breakpoint()
        
        for hype_links in link_list:
            if (("/wiki/" in hype_links) and ("File" not in hype_links) and 
                ("/wiki/Special" not in hype_links) and ("http" not in hype_links)
                and ("wiki/Help" not in hype_links) and ("Template" not in hype_links)
                and ("Wikipedia:" not in hype_links) and 
                ("Category:" not in hype_links) 
                and ("disambiguation" not in hype_links)
                and ("identifier" not in hype_links) 
                and (replace_all(seed,{ "/wiki/": "", "_": " "}).upper() not in hype_links.upper())):
                final_list.append(hype_links)
        
        final_list = list(dict.fromkeys(final_list))        
        
        return final_list
    except:
        final_list = "err"
        return final_list
        
        
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


#main loop
quit_key  = 'y'
while quit_key != "n":
    seed = "/wiki/"+ r.choice(animals)
    if " " in seed:
        seed = seed.replace(" ","_")
        
    wiki_list = bouncer(seed)    
   
    d = { "/wiki/": "", "_": " "}
    
    
    
    
    if wiki_list != "err":
        for i in range(0, 10):
            print(replace_all(r.choice(wiki_list),d))
            
       
        user_input = input("whacha think it is? ")
        
        if user_input.upper() in seed.upper():
            print ("You're Right! it was a " +replace_all(seed, d))
        else:
            print ("No you dummy! it was a " +replace_all(seed, d))
    else:
        print(seed + " not a valid wiki article")
    quit_key = input("\n \n \n Try again? y/n \n")
    
    
   
        
