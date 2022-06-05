
#Import the requisite library
from distutils.ccompiler import gen_preprocess_options
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")
text = "In the Tales of Justin, Justin Neo lives in Punggol which is situated in Singapore"
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [
                {"label": "Story","pattern": "Tales of Justin"}
]
ruler.add_patterns(patterns)
doc = nlp(text)
for ent in doc.ents:
    print(ent.text,ent.label_)
    if ent.label_ == 'GPE':
        print(ent.text)

d = {'hi':1,'no':2}
if 'hi' in d:
    print(d['hi'])
