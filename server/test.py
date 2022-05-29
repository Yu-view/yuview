from sqlite3 import TimestampFromTicks
import spacy
nlp = spacy.load("en_core_web_md")
# text = nlp(data)
text = "Love the color! Super worth the price! Thanks seller for the speedy reply and restock pink for me! i didnt know it is not compatible to macbook but itsokay i keep it cause i really love the colour and the way it sound"
doc = nlp(text)

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
                if token.similarity(doc2) < 0.95:
                    continue
                elif token.similarity(doc2)>= 0.95:
                    check=True
                    d[term] += 1
                    break
            if check==False:
                d[token.text] = 1
    print(d)

def summary_adjectives(doc):
    adjectives = ""
    for token in doc:
        if token.pos_ == 'ADJ' and token.text not in adjectives:
            adjectives += token.text + " "
    adjectives_nlp = nlp(adjectives)
    return summary(adjectives_nlp)

def summary_adverbs(doc):
    adverbs = ""
    for token in doc:
        if token.pos_ == 'ADV' and token.text not in adverbs:
            adverbs += token.text + " "
        # if token.text == 'not' or token.text =='Not' or token.text =='nt':
        #     adverbs += token.text + " "
    adverbs_nlp = nlp(adverbs)
    return summary(adverbs_nlp)

summary_adjectives(doc)
summary_adverbs(doc)
