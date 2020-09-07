import requests
import bs4
import sys
root = "C:\\Users\\lenovo\\Downloads\\django\\myProject\\home\\"
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
    url2 = root+"hespress\\"+ url+".txt"
    myArticle = ""
    with open(url2, "w", encoding="utf-8") as f :
        f.write(title)
        f.write("\n")
        for p in article :
            for text in p :
                if text.string != None :
                    f.write(text.string)
                    myArticle += text.string
                    myArticle += " "
        f.write("\n")
        f.close() 
    url = "hespress\\"+ url +".txt"
    return url,image,myArticle

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
    url2 = root+"afrique360\\"+ url+".txt"
    f = open(url2, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    for text in chapeau :
        if text.string != None :
            f.write(text.string)
    f.write("\n")
    myArticle = ""
    for text in content :
        if text.string != None :
            if ">>>LIRE AUSSI:" not in text.string :
                f.write(text.string)
                myArticle += text.string
                myArticle += " "
    f.write("\n")
    f.close()
    url = "afrique360\\"+ url+".txt"
    return url,image,myArticle

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
    url2 = root+"le360\\"+ url+".txt"
    f = open(url2, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    myArticle = ""
    if type(article) == str :
        f.write(article)
        myArticle += article.strip()
    else :
        for p in article :
            for text in p :
                if text.string != None :
                    f.write(text.string)
                    myArticle += text.string.strip()
                    myArticle += " "
    f.write("\n")
    f.close()
    url = "le360\\"+ url+".txt"
    return url,image,myArticle

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
    url2 = root+"leseco\\"+ url+".txt"
    f = open(url2, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    myArticle = ""
    for p in article :
        for text in p :
            if text.string != None :
                f.write(text.string)
                myArticle += text.string
                myArticle += " "
    f.write("\n")
    f.close()
    url = "leseco\\"+ url+".txt"
    return url,image,myArticle

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
    url2 = root+"sport360\\"+ url+".txt"
    f = open(url2, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    myArticle = ""
    for text in chapeau :
        if text.string != None :
            f.write(text.string)
            myArticle += text.string.strip()
            myArticle += " "
    f.write("\n")
    for p in article :
        for text in p :
            if text.string != None :
                f.write(text.string)
                myArticle += text.string.strip()
                myArticle += " "
    f.write("\n")
    f.close()
    url = "sport360\\"+ url+".txt"
    return url,image,myArticle 

def welovebuzz(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content,"lxml")
    title = soup.find("h2",{"id":"title"}).string
    content = soup.find("div",{"class":"article_content"})
    article = content.find_all('p')
    url = url.replace('https://www.welovebuzz.com/','')
    url = url.replace("/",'')   
    url2 = root+"welovebuzz\\"+ url+".txt"
    f = open(url2, "w", encoding="utf-8")
    f.write(title)
    f.write("\n")
    myArticle = ""
    for p in article :
        for text in p :
            if text.string != None :
                if "Publicité" not in text.string:
                    f.write(text.string)
                    myArticle += text.string
                    myArticle += " "
    f.write("\n")
    f.close()
    image = soup.find("div",{"class":"article_content"})
    image = image.find("img")
    if(image == None) :
        image = "welovebuzz"
    else : 
        image = image["src"]
    url = "welovebuzz\\"+ url+".txt"
    return url,image,myArticle 

