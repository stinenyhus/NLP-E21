from typing import List
from datasets import load_dataset
import gensim.downloader as api


# DATASET
dataset = load_dataset("conllpp")
train = dataset["train"]

#inspect the dataset
num_classes = train.features["ner_tags"].feature.num_classes
classes = train.features["ner_tags"].feature



# CONVERTING EMBEDDINGS
import numpy as np

import torch

model = api.load("glove-wiki-gigaword-50")

from embedding import gensim_to_torch_embedding

# convert gensim word embedding to torch word embedding
embedding_layer, vocab = gensim_to_torch_embedding(model)

# PREPARING A BATCH


def tokens_to_idx(tokens: List[str], vocab:dict=model.key_to_index):
    """
    tokens is a list of strings to look up in the dictionary
    If the string is not in the dictionary, it is assigned the value unknown
    returns a list of indexes for tokens in the list
    """
    return [vocab.get(t.lower(), vocab["UNK"]) for t in tokens]

# sample batch of 10 sentences
batch_tokens = train["tokens"][:10]
batch_tags = train["ner_tags"][:10]
batch_tok_idx = [tokens_to_idx(sent) for sent in batch_tokens]
batch_size = len(batch_tokens) #Number of texts

# compute length of longest sentence in batch
batch_max_len = max([len(s) for s in batch_tok_idx])
print(batch_max_len) #largest text

# prepare a numpy array with the data, initializing the data with 'PAD'
# and all labels with -1; initializing labels to -1 differentiates tokens
# with tags from 'PAD' tokens
batch_input = vocab["PAD"] * np.ones((batch_size, batch_max_len))
batch_labels = -1 * np.ones((batch_size, batch_max_len))

# copy the data to the numpy array
for i in range(batch_size):
    tok_idx = batch_tok_idx[i]
    tags = batch_tags[i]
    size = len(tok_idx)

    batch_input[i][:size] = tok_idx
    batch_labels[i][:size] = tags


# since all data are indices, we convert them to torch LongTensors
batch_input, batch_labels = torch.LongTensor(batch_input), torch.LongTensor(
    batch_labels) #Long tensors are integers - so it is because we work with integers

# CREATE MODEL
from LSTM import RNN

model = RNN(
    embedding_layer=embedding_layer, output_dim=num_classes + 1, hidden_dim_size=256
)

# FORWARD PASS
X = batch_input
y = model(X)

loss = model.loss_fn(outputs=y, labels=batch_labels)
# loss.backward()