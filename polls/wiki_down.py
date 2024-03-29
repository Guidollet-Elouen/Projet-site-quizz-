import requests
import sqlite3
from bs4 import BeautifulSoup
import random
from .config import road


#conn = sqlite3.connect(road)
#cur = conn.cursor()
#Table_wiki ='''CREATE TABLE IF NOT EXISTS WIKI(title TEXT,header TEXT,link TEXT)'''  #Create Table
#cur.execute(Table_wiki)
#cur.execute("""DROP TABLE WIKI""") #Destroy Table
#conn.commit()
#conn.close()

#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "html.parser")

def get_title(soup):
    title=soup.title.string
    i=0
    while title[i:i+len("- Wikipedia")]!="- Wikipedia":
        i+=1
    return title[0:i]

def search(word,text,limit):
    i=0
    while text[i:i+len(word)]!=word and i<=len(text):
        i+=1
        if text[i:i+len(limit)]==limit:
            return False
    return text[0:i]

def cut_wiki_header(word,text):
    i=0
    while text[i:i+len(word)]!=word and i<=len(text):
        i+=1
    return text[i+len(word):]

def get_header(soup):
    first_cut=search("Contents",soup.getText(),"References[edit]")
    if first_cut==False:
        return False
    second_cut=cut_wiki_header("Jump to search",first_cut)
    return second_cut

def insertion_wiki(link): #Insert a page "link" in the database
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    title=get_title(soup)
    header=get_header(soup)
    if header==False:
        return "not enough infos"
    print(title,header)
    confirm=input("Voulez vous entrez ses infos dans la base, si oui tapez 0 : ")
    if confirm!="0":
        return "not confirmed"
    conn = sqlite3.connect(road)
    cur = conn.cursor()
    Insert_wiki =f'''INSERT INTO WIKI(title,header,link) VALUES ('{str(title)}','{str(header)}','{str(link)}')'''
    #Insert_wiki =f'''INSERT INTO WIKI(title,header,link) VALUES ('{str(title)}',header=%(header)s,"{str(link)}"''' , {'header': str(header)}
    cur.execute(Insert_wiki)
    conn.commit()
    conn.close()
    return "confirmed"

def get_wiki(): #Get a page from the database
    conn = sqlite3.connect(road)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM WIKI''') #read the table
    result = cur.fetchall()
    random_choice=random.randrange(len(result))
    conn.close()
    return (result[random_choice][0],result[random_choice][1],result[random_choice][2])

#URL = "https://en.wikipedia.org/wiki/Special:Random"
#URL = "https://en.wikipedia.org/wiki/List_of_Super_Fight_League_champions"

