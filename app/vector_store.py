import faiss
import numpy as np
import os

class VectorStore:
    def __init__(self, dimension, index_path="data/faiss.index"):
        self.dimension = dimension
        self.index_path = index_path
        self.id_map = []

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self._load_ids()
        else:
            self.index = faiss.IndexFlatL2(dimension)

    def add(self, vector_id, vector):
        vector = np.asarray(vector, dtype=np.float32)
        self.index.add(vector[np.newaxis])
        self.id_map.append(vector_id)

    def query(self, query_vector, k=5):
        query_vector = np.asarray(query_vector, dtype=np.float32).reshape(1, -1)
        distances, indices = self.index.search(query_vector, k)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.id_map):
                sim = 1 / (1 + dist)
                results.append((self.id_map[idx], sim))
        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".ids", "w") as f:
            for vid in self.id_map:
                f.write(vid + "\n")

    def _load_ids(self):
        with open(self.index_path + ".ids", "r") as f:
            self.id_map = [line.strip() for line in f]
