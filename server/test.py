import spacy
nlp = spacy.load("en_core_web_md")  
doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
print(doc1, "<->", doc2, doc1.similarity(doc2))


french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))

