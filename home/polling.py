import requests
import polling2
import bs4


def test(response):
    return response.status_code == 200


def hespress_polling():
    links = []
    result = polling2.poll(lambda: requests.get('https://fr.hespress.com/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "h24-b"})
    titles = content.find_all("h3")
    for a in content.find_all("a", href=True, text=True):
        links.append(a["href"])
    last_link = links[0]
    last_title = titles[0].string
    return last_link, last_title
# last_link,last_title = hespress_polling()
# print(last_link,last_title)


def is_last_hespress(last_title):
    last_link2, last_title2 = hespress_polling()
    while(last_title == last_title2):
        last_link2, last_title2 = hespress_polling()
    else:
        process(last_link2)


def afrique360_polling():
    links = []
    result = polling2.poll(lambda: requests.get('http://afrique.le360.ma/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "view-display-id-chrono_list"})
    # print(content)
    titles = content.find_all("a")
    for a in content.find_all("a", href=True, text=True):
        a["href"] = a["href"].replace("/", "http://afrique.le360.ma/", 1)
        links.append(a["href"])
    last_link = links[0]
    last_title = titles[1].string
    return last_link, last_title
# last_link,last_title = afrique360_polling()
# print(last_link,last_title)


def le360_polling():
    links = []
    result = polling2.poll(lambda: requests.get('https://fr.le360.ma/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "post-holder"})
    # print(content)
    titles = content.find_all("a")
    # print(titles)
    for a in content.find_all("a", href=True, text=True):
        a["href"] = a["href"].replace("/", "https://fr.le360.ma/", 1)
        links.append(a["href"])
    last_link = links[0]
    last_title = titles[1].string
    return last_link, last_title
# last_link,last_title = le360_polling()
# print(last_link,last_title)


def sport360_polling():
    links = []
    result = polling2.poll(lambda: requests.get('https://sport.le360.ma/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "page swiper-slide"})
    # print(content)
    titles = content.find_all("span", {"class": "contenu"})
    # print(titles[0].text)
    for a in content.find_all("a"):
        links.append(a["href"])
    last_link = links[0]
    last_title = titles[0].text
    return last_link, last_title
# last_link,last_title = sport360_polling()
# print(last_link,last_title)



def welovebuzz_polling():
    links = []
    result = polling2.poll(lambda: requests.get('https://www.welovebuzz.com/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "row"})
    # print(content)
    titles = content.find_all("a")
    # print(titles)
    for a in content.find_all("a"):
        links.append(a["href"])
    # print(links[0])
    i = 0
    links2 = []
    while(i < len(links)):
        links2.append(links[i])
        i += 3
    last_link = links2[0]
    last_title = titles[0].text
    return last_link, last_title
# last_link,last_title = welovebuzz_polling()
# print(last_link,last_title)



def leseco_polling():
    links = []
    titles = []
    result = polling2.poll(lambda: requests.get('https://leseco.ma/', timeout=5),
                           step=60,
                           poll_forever=True,
                           ignore_exceptions=(
                               requests.exceptions.ConnectionError,),
                           check_success=test)
    soup = bs4.BeautifulSoup(result.content, "lxml")
    content = soup.find("div", {"class": "slide"})
    # print(content)
    for a in content.find_all("a", href=True):
        if(a.get("aria-label") != None):
            titles.append(a.get("aria-label"))
    # print(titles)
    for a in content.find_all("a"):
        links.append(a["href"])
    i = 0
    links2 = []
    while(i < len(links)):
        links2.append(links[i])
        i += 2
    last_link = links2[0]
    last_title = titles[0]
    return last_link, last_title
# last_link,last_title = leseco_polling()
# print(last_link,last_title)
