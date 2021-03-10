import nltk
import warnings
from nltk.corpus import stopwords
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('punkt')
import threading

language='portuguese'

def LemTokens(tokens):
    #lemmer = nltk.stem.WordNetLemmatizer()
    lemmer = nltk.stem.RSLPStemmer()
#    return [lemmer.lemmatize(token) for token in tokens]
    return [lemmer.stem(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def similarity(user_response,text):
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import TfidfVectorizer
    sent_tokens = nltk.sent_tokenize(text, language=language)
    sent_tokens.append(user_response.lower())
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=stopwords.words(language))
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    #sent_tokens.remove(user_response.lower())
    return req_tfidf