import spacy
import os
from collections import Counter

path = "/work/Classes_syllabus/NLP-E21/syllabus/classes/data/train_corpus"
def corpus_loader(folder: str = path):
    """
    A corpus loader function which takes in a path to a 
    folder and returns a list of strings.
    """
    file_list = os.listdir(folder)
    return file_list

def text_loader(path):
    texts = []
    for file in corpus_loader(path)[:5]:
        with open(f"{path}/{file}") as f:
            texts.append(f.read())
    return texts

texts = text_loader(path)
nlp = spacy.load("en_core_web_sm")
docs = nlp(texts[0])

##1
def extract_lemmas(docs, lemma_classes = ["NOUN", "ADJ", "VERB"]):
    lemmas_keep = []
    for doc in docs:
        if doc.pos_ in lemma_classes:
            lemmas_keep.append(doc.lemma_)
    return lemmas_keep

def POS_ratio(docs):
    POStags = [doc.pos_ for doc in docs]
    unique_tags = set(POStags)
    counts = {tag:POStags.count(tag) for tag in unique_tags}
    ratios = {tag:round(counts[tag]/len(POStags),3) for tag in unique_tags}
    return counts, ratios

def POS_ratio_2(docs):
    counts = Counter([doc.pos_ for doc in docs])
    ratios = {tag:count/len(docs) for tag,count in counts.items()}
    return ratios

def MDD(docs):
    distances = [abs(doc.head.i - doc.i) for doc in docs]
    return sum(distances)/len(distances)

# print(extract_lemmas(docs))
# print(POS_ratio_2(docs))
# print(POS_ratio(docs))
print(MDD(docs))
