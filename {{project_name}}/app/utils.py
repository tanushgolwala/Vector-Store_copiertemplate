import numpy as np

def sentence_to_vector(sentence, wordtoidx):
    vector = np.zeros(len(wordtoidx))
    for token in sentence.lower().split():
        if token in wordtoidx:
            vector[wordtoidx[token]] += 1
    return vector
