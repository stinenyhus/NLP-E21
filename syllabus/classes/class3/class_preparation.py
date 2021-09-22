import spacy
import os
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")
token = doc[1]
print(dir(token))

def corpus_loader(folder: str = "/work/Classes_syllabus/NLP-E21/syllabus/classes/data/train_corpus"):
    """
    A corpus loader function which takes in a path to a 
    folder and returns a list of strings.
    """
    file_list = os.listdir(folder)
    return file_list

print(corpus_loader())