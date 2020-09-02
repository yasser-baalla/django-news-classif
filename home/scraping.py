import requests
import bs4
import sys

def hespress(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    title = soup.find("h1").string
    content = soup.find("div",{"class":"content"})
    image = content.find("img")
    image = image["src"]
    article = content.find_all('p')
    url = url.replace('https://fr.hespress.com/','')
    url = url.replace(".html",'')
    url = "hespress\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for p in article :
        for text in p :
            if text.string != None :
                f.write(text.string)
    f.write("\n")
    f.close()
    return url,image

def afrique(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    image = soup.find("div",{"class":"holder_img"})
    image = image.find("img")
    image = image["src"]
    title = soup.find("h1",{"class":"ttl"}).string
    chapeau = soup.find("p",{"class":"catchline"})
    content = soup.find("div",{"id":"content"})
    url = url.split("/")
    url = url[len(url)-1]
    url = "afrique.le360\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for text in chapeau :
        if text.string != None :
            f.write(text.string)
    f.write("\n")
    for text in content :
        if text.string != None :
            if ">>>LIRE AUSSI:" not in text.string :
                f.write(text.string)
    f.write("\n")
    f.close()
    return url,image

def le360(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    image = soup.find("div",{"class":"full-item"})
    image = image.find("img")
    image = image["src"]
    content = soup.find("div",{"class":"articles-holder"})
    title = content.find("h1").string
    content = soup.find("div",{"class":"ctn"})
    if content == None :
        content = soup.find("div",{"class":"wording-article"})
        article = str(content.find('p').string)
    else :
        article = content.find_all('p')
    url = url.split("/")
    url = url[len(url)-1]
    url = "le360\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    if type(article) == str :
        f.write(article)
    else :
        for p in article :
            for text in p :
                if text.string != None :
                    f.write(text.string)
    f.write("\n")
    f.close()
    return url,image

def leseco(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    image = soup.find("div",{"class":"featured-area"})
    image = image.find("img")
    image = image["src"]
    title = soup.find("h1",{"class":"post-title entry-title"}).string
    content = soup.find("div",{"class":"entry-content entry clearfix"})
    article = content.find_all('p')
    url = url.replace('https://leseco.ma/','')
    url = url.replace("/",'')
    url = "leseco\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for p in article :
        for text in p :
            if text.string != None :
                f.write(text.string)
    f.write("\n")
    f.close()
    return url,image

def sport(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    image = soup.find("div",{"class":"image"})
    image = image.find("img")
    image = image["src"]
    title = soup.find("h1",{"class":"titre-article"}).string
    chapeau = soup.find("div",{"class":"chapeau"})
    content = soup.find("div",{"class":"wysiwyg"})
    article = content.find_all('p')
    url = url.split("/")
    url = url[len(url)-1]
    url = "sport.le360\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for text in chapeau :
        if text.string != None :
            f.write(text.string)
    f.write("\n")
    for p in article :
        for text in p :
            if text.string != None :
                f.write(text.string)
    f.write("\n")
    f.close()
    return url,image

def welovebuzz(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    image = soup.find("div",{"class":"article_content"})
    image = image.find("img")
    image = image["src"]
    title = soup.find("h2",{"id":"title"}).string
    content = soup.find("div",{"class":"article_content"})
    article = content.find_all('p')
    url = url.replace('https://www.welovebuzz.com/','')
    url = url.replace("/",'')   
    url = "welovebuzz\\"+ url+".txt"
    f = open(url, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for p in article :
        for text in p :
            if text.string != None :
                if "Publicité" not in text.string:
                    f.write(text.string)
    f.write("\n")
    f.close()
    return url,image
