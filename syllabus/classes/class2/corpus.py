'''
This class does this
'''
import os

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
    
    def segment_sentences(self, by = "."):
        self.sentences = [text.split(".") for text in self.texts]

test_corpus = corpus("/work/NLP-E21/syllabus/classes/class2/train_corpus")
test_corpus.segment_sentences()
print(test_corpus.sentences[1])




    