# POSTGRES BASED VECTOR STORE FOR RAG EMBEDDING

A production-ready vector search API using **FastAPI**, **FAISS**, and **PostgreSQL**. Easily scalable, containerized with Docker, and modularized for rapid development of search-based ML systems.

---

## 🚀 Features

- 🔎 **FAISS**: High-performance vector similarity search
- 🗃️ **PostgreSQL**: Stores metadata and vector blobs
- ⚡ **FastAPI**: RESTful API for vector `add` and `query`
- 🐳 **Docker Compose**: Modular dev environment
- 📦 **Copier Template Ready**: Scaffold new search apps in seconds

---

## 💾 Data Storage

- **Vectors**: Stored in FAISS index at `data/faiss.index`
- **ID map**: Stored in `data/faiss.index.ids`
- **Metadata**: Stored in PostgreSQL (`vectors` table)

---

## 🧰 Tech Stack

- FAISS (vector index)
- SQLAlchemy (ORM)
- PostgreSQL (database)
- FastAPI (API framework)
- Docker (runtime isolation)
- Copier (template engine)

---

# 📦 How to Use This Copier Template

This guide explains how to use the Copier template to scaffold a new vector search project.

---

## ✅ Prerequisites

- Python 3.12+
- [Copier](https://copier.readthedocs.io) installed:
  ```bash
  pip install copier
  ```

---

## 🚀 Generate a New Project

```bash
copier copy gh:your-username/vector-search-template my-new-project
```

This will prompt:

```
What is the name of your project? → My Vector Search App
Slug for directory/project name? → my_vector_search_app
```

---

## 🔌 API Usage

### ➕ Add a Sentence

```bash
curl -X POST http://localhost:8000/add \
  -H "Content-Type: application/json" \
  -d '{"text": "The quick brown fox jumps over the lazy dog"}'
```

### 🔍 Query Similar Sentences

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"text": "brown fox jumps"}'
```

---
