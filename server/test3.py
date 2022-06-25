import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import json
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
nlp1 = spacy.load("en_core_web_md")
data = open('mockdata.json')
y = json.load(data)

lst = []
for lists in y:
    if 'comment' in lists:
            lst.append([lists['comment']])
string = ''
for list in lst:
    string += list[0]

doc = nlp(string)

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

print(positive_words)
print(total_pos)
