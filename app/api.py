from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import VectorEntry
from app.vector_store import VectorStore
from app.utils import sentence_to_vector
import numpy as np
import uuid
import os

router = APIRouter()
DIM = 100 
store = VectorStore(dimension=DIM)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

wordtoidx = {}  # Fill dynamically

@router.post("/add")
def add_vector(text: str, db: Session = Depends(get_db)):
    global wordtoidx
    for word in text.lower().split():
        if word not in wordtoidx:
            wordtoidx[word] = len(wordtoidx)

    vec = sentence_to_vector(text, wordtoidx)
    vec_blob = vec.astype(np.float32).tobytes()
    vector_id = str(uuid.uuid4())

    db.add(VectorEntry(id=vector_id, text=text, embedding=vec_blob))
    db.commit()

    store.add(vector_id, vec)
    store.save()

    return {"id": vector_id, "message": "Vector added."}

@router.post("/query")
def query(text: str):
    vec = sentence_to_vector(text, wordtoidx)
    results = store.query(vec)
    return {"results": results}
