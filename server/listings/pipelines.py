# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import spacy
from scrapy.utils.defer import maybe_deferred_to_future
class ShopeePipeline:

    def open_spider(self, spider):
        self.nlp = spacy.load("en_core_web_md")

    async def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        reviews = adapter.get("reviews")
        data = self.nlp("".join(map(lambda x: x['comment'] if 'comment' in x else '', reviews)))
        adapter["sum_adj"] = self.summary_adjectives(data)
        adapter["sum_adv"] = self.summary_adverbs(data)

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


'''
{
        "name": "CIY Tester 68 TES68 / GK68 Keyboard Kit",
        "rating": 4.826086956521739,
        "price": 32.0,
        "num_rating": 23,
        "num_sold": 54,
        "item_id": 14145141032,
        "shop_id": 86538976,
        "reviews": [
            {
                "model": [
                    "Transparent Lavender"
                ]
            },
            {
                "model": [
                    ""
                ]
            },
            {
                "model": [
                    ""
                ]
            },
            {
                "model": [
                    ""
                ],
                "comment": "Very fast delivery.ordered on 7 and received on the 10th and friendly seller"
            },
            {
                "model": [
                    ""
                ],
                "comment": "the seller has very kind and is very fast with the orders! product was good and the delivery was reliable!! definitely would buy again!! 100% recommend this shop."
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "Transparent Lavender"
                ]
            },
            {
                "model": [
                    "Transparent Black"
                ]
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    ""
                ],
                "comment": "All good!"
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "Transparent Emerald"
                ]
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "Transparent Black"
                ]
            },
            {
                "model": [
                    "White"
                ]
            },
            {
                "model": [
                    "Transparent Emerald"
                ],
                "comment": "Bought this to make use of my spare switches laying around. Really like the colour and the quality. Connectivity works as expected and item was received in 2 days! Thanks seller!"
            },
            {
                "model": [
                    "White"
                ],
                "comment": "Product is as described. Wrapped in pe foam. Extremely fast delivery. Arrived in less than 24 hours. Very solid. And average stabs. Haven't put switches in yet though. But very nice budget keeb."
            },
            {
                "model": [
                    ""
                ],
                "comment": "I received the product the next day after buying. The board is amazing with foam and everything."
            }
}
'''