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
    
    def segment_sentences(self, by = ["! ", ". ", "; ", ": ", "? ", " - "], lower_case = False):
        pattern = '|'.join('(?<={})'.format(re.escape(delim)) for delim in by)
        self.sentences = [re.split(pattern, text) for text in self.texts]
        self.sentences = [[sent.lstrip() for sent in sentences] for sentences in self.sentences]
        self.sentences = [[sent for sent in sentences if sent not in ['', ' ', '" ', "!", "?"]] for sentences in self.sentences]
        if lower_case:
            self.sentences = [[sent.lower() for sent in sentences] for sentences in self.sentences]

    def tokenize_sentences(self):
        self.token_lists = [[re.findall(r"[\w']+", sent) for sent in sentences] for sentences in self.sentences]
        self.tokens = [[token for t_list in token_lists for token in t_list] for token_lists in self.token_lists]

    def calculate_PMI(self):
        self.word_sets = [set(tokens) for tokens in self.tokens]
        self.word_freqs = []
        for word_set, tokens in zip(self.word_sets,self.tokens):
            self.word_freqs.append({word:tokens.count(word) for word in word_set})
        self.bigram_freqs = []
        for token_list in self.tokens:
            bigrams = [f'{token_list[i]}_{token_list[i+1]}' for i in range(len(token_list)-1)]
            self.bigram_freqs.append({bigram:bigrams.count(bigram) for bigram in bigrams})

test_corpus = corpus("/work/StineNyhusLarsen#2609/Jobs/Coder Python/Class_1609-b00c9c19/NLP-E21/syllabus/classes/class2/train_corpus")
test_corpus.segment_sentences(lower_case=True) 
test_corpus.tokenize_sentences()
test_corpus.calculate_PMI()
print(test_corpus.bigram_freqs[0])
# print(test_corpus.texts[2], test_corpus.word_sets[2], test_corpus.sentences[2], test_corpus.tokens[2], sep = "\n")
# print(test_corpus.texts[1], test_corpus.sentences[1], sep = "\n")