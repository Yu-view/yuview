# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import spacy
from scrapy.utils.defer import maybe_deferred_to_future
from scrapy.exceptions import DropItem

class ShopeePipeline:

    def open_spider(self, spider):
        self.nlp = spacy.load("en_core_web_md")

    async def process_item(self, item, spider):
        if not item:
            raise DropItem("Missing listing")
        else:
            adapter = ItemAdapter(item)
            reviews = adapter.get("reviews")
            data = self.nlp("".join(map(lambda x: x['comment'] if 'comment' in x else '', reviews)))
            adapter["sum_adj"] = self.summary_adjectives(data)
            adapter["sum_adv"] = self.summary_adverbs(data)
            return item



    def summary(self, doc):
        d = {}
        for token in doc:
            if token.text not in d and len(d) == 0:
                d[token.text] = 1
            elif token.text in d:
                d[token.text] += 1
            else:
                check=False
                for term in d:
                    doc2 = self.nlp(term)
                    if token.similarity(doc2) < 0.75:
                        continue
                    elif token.similarity(doc2)>= 0.75:
                        check=True
                        d[term] += 1
                        break
                if check==False:
                    d[token.text] = 1
        return d

    def summary_adjectives(self, doc):
        adjectives = ""
        for token in doc:
            if token.pos_ == 'ADJ' and token.text not in adjectives and token.has_vector == True:
                adjectives += token.text + " "
        adjectives_nlp = self.nlp(adjectives)
        return self.summary(adjectives_nlp)

    def summary_adverbs(self, doc):
        adverbs = ""
        for token in doc:
            if token.pos_ == 'ADV' and token.text not in adverbs and token.has_vector == True:
                adverbs += token.text + " "
            # if token.text == 'not' or token.text =='Not' or token.text =='nt':
            #     adverbs += token.text + " "
        adverbs_nlp = self.nlp(adverbs)
        return self.summary(adverbs_nlp)