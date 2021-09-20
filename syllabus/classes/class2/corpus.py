'''
This class does this
'''
import os
import re

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

class corpus:
    def __init__(self, path):
        self.texts = []
        self.ids = []
        os.chdir(path)
        # iterate through all file
        for file in os.listdir():
            self.ids.append(str(file[:-4]))
            self.texts.append(str(read_text_file(f"{path}/{file}")))
    
    def segment_sentences(self, by = "[!|.]"):
        self.sentences = [re.split(by, text) for text in self.texts]
        self.sentences = [sent for sent in self.sentences if sent != " "]
        # for char in by[1:]:
        #     self.sentences = [text.split(char) for text in self.sentences]

    def tokenize_sentences(self, readline):
        self.tokens = [re.findall(r"[\w']+", text) for text in self.texts]

test_corpus = corpus("/work/StineNyhusLarsen#2609/Jobs/Coder Python/Class_1609-b00c9c19/NLP-E21/syllabus/classes/class2/train_corpus")
test_corpus.segment_sentences() 
print(test_corpus.texts[1], test_corpus.sentences[1], sep = "\n")




    