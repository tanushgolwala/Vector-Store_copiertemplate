import faiss
import numpy as np
import os

class VectorStore:
    def __init__(self, dimension, index_path="vector.index"):
        self.dimension = dimension
        self.index_path = index_path
        self.id_map = []

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self.id_map = self._load_id_map(index_path + ".ids")
        else:
            self.index = faiss.IndexFlatL2(dimension)

    def add_vector(self, vector_id, vector):
        vector = np.asarray(vector, dtype=np.float32)
        if vector.shape[0] != self.dimension:
            raise ValueError("Vector dimension mismatch.")
        self.index.add(np.expand_dims(vector, axis=0))
        self.id_map.append(vector_id)

    def findsimvectors(self, queryvec, maxres=5):
        queryvec = np.asarray(queryvec, dtype=np.float32)
        queryvec = np.expand_dims(queryvec, axis=0)
        distances, indices = self.index.search(queryvec, maxres)

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

    def _load_id_map(self, id_path):
        with open(id_path, "r") as f:
            return [line.strip() for line in f]
