import spacy
nlp = spacy.load("en_core_web_sm")
text = 'ur mum gay'
test = nlp (text)
for token in test:
    print(token)
print ("hello")
