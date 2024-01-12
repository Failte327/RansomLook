import os
from bs4 import BeautifulSoup
from typing import Dict, List

def main() -> List[Dict[str, str]] :
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('div', {"class": "carts-section__item"})
                for div in divs_name:
                    title = div.find('h2').text.strip()
                    description = div.find('div',{"class" : "cart-block__content"}).text.strip()
                    try:
                        list_div.append({"title" : title, "description" : description, "link" : div.a['href'], "slug": filename})
                    except:
                        list_div.append({"title" : title, "description" : description})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
