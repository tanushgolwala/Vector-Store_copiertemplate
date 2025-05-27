import numpy as np


class VectorStore:
    def __init__(self, dimension):
        self.vector_data = {}
        self.vector_index = {}

    def add_vector(self, vector_id, vector):

        self.vector_data[vector_id] = vector
        self.update_vector(vector_id, vector)

    def get_vector(self, vector_id):
        if vector_id not in self.vector_data:
            raise KeyError(f"Vector ID {vector_id} not found.")
        return self.vector_data.get(vector_id)

    def update_vector(self, vector_id, new_vector):
        for eid, evec in self.vector_data.items():
            sim = np.dot(evec, new_vector) / \
                (np.linalg.norm(evec) * np.linalg.norm(new_vector))
            if eid not in self.vector_index:
                self.vector_index[eid] = {}
            self.vector_index[eid][vector_id] = sim

    def findsimvectors(self, queryvec, maxres=5):
        res = []
        for vector_id, vector in self.vector_data.items():
            sim = np.dot(vector, queryvec) / \
                (np.linalg.norm(vector) * np.linalg.norm(queryvec))
            res.append((vector_id, sim))
        res.sort(key=lambda x: x[1], reverse=True)
        return res[:maxres]
