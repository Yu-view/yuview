import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import json
import time
import scrapy
from scrapy.crawler import CrawlerProcess
from listings.spiders.shopee import ShopeeSpider

start_time = time.time()
process = CrawlerProcess()
data = open('test.json')
y = json.load(data)
# print(y[1])
lst = []
for lists in y:
    reviews = lists['reviews']
    for review in reviews:
        if 'comment' in review:
            lst.append([review['comment']])
string = ''
for list in lst:
    string += list[0]
# print(string)
nlp1 = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_md")
nlp.add_pipe('spacytextblob')
datas = nlp(string)

def reviews_str(data,name):
    lst = []
    for lists in data:
        if lists['name'] == name:
            reviews = lists['reviews']
            for review in reviews:
                if 'comment' in review:
                    lst.append([review['comment']])
    string = ''
    for list in lst:
        string += list[0]
    return string

doc = nlp1(string)

positive_words = []
negative_words = []
total_pos = []
total_neg = []
for x in datas._.blob.sentiment_assessments.assessments:
  if x[1] > 0:
    positive_words.append(x[0][0])
  elif x[1] < 0:
    negative_words.append(x[0][0])
  else:
    pass
total_pos.append(', '.join(set(positive_words)))
total_neg.append(', '.join(set(negative_words)))
# print(positive_words)
# print(negative_words)
# print(total_pos)

def summary(doc):
    d = {}
    for token in doc:
        if token.text not in d and len(d) == 0:
            d[token.text] = 1
        elif token.text in d:
            d[token.text] += 1
        else:
            check=False
            for term in d:
                doc2 = nlp(term)
                if token.similarity(doc2) < 0.75:
                    continue
                elif token.similarity(doc2)>= 0.75:
                    check=True
                    d[term] += 1
                    break
            if check==False:
                d[token.text] = 1
    print(d)

def summary_adjectives(doc):
    adjectives = ""
    for token in doc:
        if token.pos_ == 'ADJ' and token.text not in adjectives and token.has_vector == True:
            adjectives += token.text + " "
    adjectives_nlp = nlp(adjectives)
    return summary(adjectives_nlp)

def summary_adverbs(doc):
    adverbs = ""
    for token in doc:
        if token.pos_ == 'ADV' and token.text not in adverbs and token.has_vector == True:
            adverbs += token.text + " "
        # if token.text == 'not' or token.text =='Not' or token.text =='nt':
        #     adverbs += token.text + " "
    adverbs_nlp = nlp(adverbs)
    return summary(adverbs_nlp)

# start_time2 = time.time()
# summary_adjectives(datas)
# start_time3 = time.time()
# summary_adverbs(nlp(reviews_str(y,"CIY Tester 68 TES68 / GK68 Keyboard Kit")))

data.close()

print("--- %s seconds ---" % (time.time() - start_time))
# print("--- %s seconds ---" % (time.time() - start_time2))
# print("--- %s seconds ---" % (time.time() - start_time3))