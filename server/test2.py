import spacy
import json
import time
start_time = time.time()
data = open('mockdata.json')
y = json.load(data)
rating_list= []
for lists in y:
    if 'Rating' in lists:
        rating_list.append(lists['Rating'])
    elif 'rating' in lists:
        rating_list.append(lists['rating'])
# print(rating_list)
# ave_rating = sum(rating_list)/len(rating_list)
# print('Average rating: ' + str(ave_rating))
lst = []
for lists in y:
    if 'comment' in lists:
            lst.append([lists['comment']])
string = ''
for list in lst:
    string += list[0]
# print(string)
nlp = spacy.load("en_core_web_md")
datas = nlp(string)
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

start_time2 = time.time()
summary_adjectives(datas)
start_time3 = time.time()
summary_adverbs(datas)

data.close()

print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time2))
print("--- %s seconds ---" % (time.time() - start_time3))
