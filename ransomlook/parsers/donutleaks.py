import os
from bs4 import BeautifulSoup # type: ignore

def main():
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('div', {"class": "box post-box"})
                for div in divs_name:
                    title = div.find('h2').text.strip()
                    description = div.find('p').text.strip()
                    list_div.append({'title':title, 'description': description})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
