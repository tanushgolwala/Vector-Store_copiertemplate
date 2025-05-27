from vector_store import VectorStore
import numpy as np

vector_store = VectorStore(dimension=3)

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends."
]


voc = set()

for i in sentences:
    tokens = i.lower().split()
    voc.update(tokens)
    
wordtoidx = {word: idx for idx, word in enumerate(voc)}

sentence_vectors = {}
for i in sentences:
    tokens = i.lower().split()
    vector = np.zeros(len(voc))
    for token in tokens:
        if token in wordtoidx:
            vector[wordtoidx[token]] += 1
    
    sentence_vectors[i] = vector


for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)

query_sentence = "Mango is the best fruit"
query_vector = np.zeros(len(voc))
query_tokens = query_sentence.lower().split()
for token in query_tokens:
    if token in wordtoidx:
        query_vector[wordtoidx[token]] += 1

similar_sentences = vector_store.findsimvectors(query_vector, maxres=2)

# Print similar sentences
print("Query Sentence:", query_sentence)
print("Similar Sentences:")
for sentence, similarity in similar_sentences:
    print(f"{sentence}: Similarity = {similarity:.4f}")