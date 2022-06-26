import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import json
import time
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from listings.spiders.shopee import ShopeeSpider

start_time = time.time()
# process = CrawlerProcess()
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
nlp = spacy.load("en_core_web_sm")
nlp1 = spacy.load("en_core_web_md")
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
positive_count = {}
negative_count = {}
for word in positive_words:
    if word not in positive_count:
        positive_count[word] = 1
    else:
        positive_count[word] += 1
for word in negative_words:
    if word not in negative_count:
        negative_count[word] = 1
    else:
        negative_count[word] += 1

def sorted(count,no):
    lst = []
    for word in count:
        lst.append([word,count[word]])
    lst.sort(key= lambda x:x[1], reverse= True)
    return(lst[0:no])

# print(positive_words)
# print(negative_words)
# print(total_pos)
# print(positive_count)
# sorted(positive_count,4)
# sorted(negative_count,4)

def common_words(count1,count2,no1,no2):
    positive = sorted(count1,no1)
    negative = sorted(count2,no2)
    positive_string = ''
    negative_string = ''
    for word in positive:
        positive_string += ', ' + word[0] + '(' + str(word[1]) + ')'
    for word in negative:
        negative_string += ', ' + word[0] + '(' + str(word[1]) + ')'
    print('Top positive words are' + positive_string +'. Top negative words are' + negative_string +'.')

# common_words(positive_count,negative_count,4,4)

def review(data,name,no1,no2):
    doc = nlp(reviews_str(data,name))
    positive_words = []
    negative_words = []
    total_pos = []
    total_neg = []
    for x in doc._.blob.sentiment_assessments.assessments:
        if x[1] > 0:
            positive_words.append(x[0][0])
        elif x[1] < 0:
            negative_words.append(x[0][0])
        else:
            pass
    total_pos.append(', '.join(set(positive_words)))
    total_neg.append(', '.join(set(negative_words)))
    positive_count = {}
    negative_count = {}
    for word in positive_words:
        if word not in positive_count:
            positive_count[word] = 1
        else:
            positive_count[word] += 1
    for word in negative_words:
        if word not in negative_count:
            negative_count[word] = 1
        else:
            negative_count[word] += 1
    for lists in data:
        if lists['name'] == name:
            print('Rating: ' + str(lists['rating']))
            print('No of ratings: ' + str(lists['num_rating']))
            print('Price: ' + str(lists['price']))
            print('Quantity sold: ' + str(lists['num_sold']))
    return common_words(positive_count,negative_count,no1,no2)

review(y,"Lifely Wireless Keyboard Mouse Set - Cutie Kitty Keyboard with Power Saving, Muted Keys, Adds Good Mood to Your WorkDesk",2,2)

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