import requests
import time
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
from pymorphy2 import MorphAnalyzer
from pymystem3 import Mystem
from transliterate import translit, get_available_language_codes


morph = MorphAnalyzer()


#make links for the proper period (July 2015 - December 2018)
def make_links():
    links = []
    for i in range(80385, 118320): # 80385 # 81288
        link = "http://www.pravoslavie.ru/" + str(i) + ".html"
        links.append(link)
    return links


# take only proper Russian articles, filter out
# not news, news taken from other sources,
# English and Serbian articles, and empty pages
def russian_links(link):
    # to sleep, get html and wait in case of connection interruption
    time.sleep(0.5)
    resp=requests.get(link, timeout=1000000)

    bs=BeautifulSoup(resp.text, "lxml")
    text_only = BeautifulSoup(" ".join([p.text for p in bs.find_all("p")]), "lxml").get_text()
    title = bs.h1

    if title == None:
        return None
    wh_author = bs.find("p")
    try:
        author = wh_author.find("a").text
    except AttributeError:
        return None
    if bs.h1 != None:
        if re.search('[a-zA-ZјJћњђљ]', bs.h1.text) is None and bs.find("p", {"class": "block-doc__date"}) is not None:
            if re.search('[ћњђљ]', text_only) is None:
                return bs, link, author
    else:
        return None


# plain_text to folder
def to_folder(bs, link, author):
    print(link)
    # make date
    date_raw = bs.find("p", {"class": "block-doc__date"}).text
    date_raw = date_raw.replace('\xa0', ' ')
    date = date_raw.split(" ")
    if date[0] == '':
        date.remove(date[0])
    year, month = date[2], morph.parse(date[1])[0].normal_form
    # make folder for years and months
    try:
        os.makedirs("./plain_text/" + year + "/" + month)
    except FileExistsError:
        pass
    path = "./plain_text/" + year + "/" + month

    # prepare articles and titles for writing
    text_only = BeautifulSoup(" ".join([p.text for p in bs.find_all("p")]), "lxml").get_text()
    text_only = re.sub(r'[\s]+', ' ', text_only)
    clean_text = re.search( r'(.*)скрыть способы оплаты скрыть способы оплаты', text_only)
    if clean_text:
        text_only = clean_text.group(1)
    #prepare name for file
    raw_title = bs.h1.text
    trans_title = translit(raw_title, 'ru', reversed=True)
    # make name prettier
    title = re.sub(r'[^\w]', '_', trans_title)
    text = raw_title + ". " + text_only
    # save plain text file
    with open(os.path.join(path, '') + title + ".txt", "w") as f:
        f.write(text)
    return date_raw, year, month, path, link, title, text, bs, author


#text to analyse using Mystem
def use_mystem(text):
    analized_article = []
    m = Mystem()
    processed = m.analyze(text)
    for w in processed:
        w_text = w["text"].lower().strip()
        if re.search('[а-яА-Яa-zA-Z]', w_text) == None:
            pass
        else:
            w = str(w)
            w = re.sub(r'[\[\}\]\{]', '', w)
            w = w.split()
          #  print(w)
            if len (w) == 9:
                parts = w[8].strip('\''), w[2].strip('\','), w[4].strip('\','), w[6].strip('\',')
                analized_words = list(parts)
                analized_article.append(analized_words)
    return analized_article


def mystemed_to_folder(date_raw, year, month, path, link, title, text, bs, author):
    # make folder for years and months
    try:
        os.makedirs("./mystem_text/" + year + "/" + month)
    except FileExistsError:
        pass
    df_my = pd.DataFrame(use_mystem(text), columns=['word', 'lex', 'wt', 'gr'])
    df_my.to_csv(os.path.join("./mystem_text/" + year + "/" + month, '') + title + ".csv", sep='\t')

    return date_raw, path, link, title, bs, text, author


# to count words
sum_of_words = 0
# collect data fot meta table
def collect_data(date_raw, path, link, title, bs, text, author):
    global sum_of_words

    date = date_raw

    source = 'Православие.Ru'

    title_better = bs.h1.text + ", " + re.sub(r'([_])\1+', r'\1', title)

    wordcount = len(text.split(' '))
    sum_of_words += wordcount
    print('Sum_of_words = ', sum_of_words)

    url = link

    data = path, author, date, source, title_better, url, wordcount

    return data


# collect ready data about article
all_data = []


def collect_ready(path, author, date, source, title, url, wordcount):
    global all_data

    all_data.append([path, author, date, source, title, url, wordcount])
    return all_data


# make a csv_file
df = pd.DataFrame

def make_tsv(all_data):
    global df

    df = pd.DataFrame(all_data, columns=['path', 'author', 'date', 'source', 'title', 'url', 'wordcount'])
    df.to_csv('meta_info.csv', sep='\t')


def main():
    # make links for the proper period (July 2015 - December 2018)
    raw_links = make_links()
    # iterate over the created links
    for raw_link in raw_links:
        link_bs = russian_links(raw_link)
        if link_bs != None:
            make_tsv(collect_ready(*collect_data(*mystemed_to_folder(*to_folder(*(link_bs))))))
        else:
            print("Bad link")
    return 0


if __name__ == '__main__':
    main()
