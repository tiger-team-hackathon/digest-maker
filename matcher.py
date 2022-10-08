import os
import string
from functools import reduce

from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from navec import Navec

from natasha import (
    Segmenter,
    MorphVocab,
    Doc
)

from natasha.doc import DocSpan


class Matcher:
    def __init__(self, role_embs):
        path = os.path.join('models', 'navec_news_v1_1B_250K_300d_100q.tar')
        self.navec = Navec.load(path)
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()

        self.stopwords = stopwords.words('russian')
        self.stopwords.extend(string.punctuation)
        self.stopwords.extend(['см', 'материалы', 'новость'])

        self.role_embs = role_embs

    def get_digest_for_role(self, role):
        role_embs = self.role_embs[role]
        role_emb = reduce(lambda a, b: a + b, role_embs)

        news = self.load_news()
        tokenized_news = self.tokenize_news(news)

        mean_embs = []

        for new in consult_news_list_tokenized:
            token_embs = []

            for token in new:
                if token in navec:
                    token_embs.append(navec[token])

            mean_embs.append(reduce(lambda a, b: a + b, token_embs) / len(token_embs))

        news_embs_df =  pd.DataFrame(mean_embs)
        # TODO

    def get_score(self, role_emb, emb):
        # TODO
        pass

    def load_news(self):
        news_path = os.path.join('news', 'cbr-400.json')
        news_df = pd.read_json(news_path)

        return news_df[['content', 'date']]

    def tokenize_news(self, news):
        news_tokenized = []

        for text in news:
            doc = Doc(text)
            doc.segment(segmenter)

            tokens_list = []

            for token in doc.tokens:
                t = normalize_span(token.text.lower())
                if t not in stopwords:
                    tokens_list.append(t)

            news_tokenized.append(tokens_list)

        return news_tokenized

    def normalize_span(span):
        entry = span.strip()

        doc = Doc(entry)
        doc.segment(self.segmenter)

        span = DocSpan(start=0,
                    stop=len(entry),
                    type='ORG',
                    text=entry,
                    tokens=[token for token in doc.tokens])

        span.normalize(self.morph_vocab)

        return span.normal