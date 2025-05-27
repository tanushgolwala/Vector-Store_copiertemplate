# 🚀 How to Run the Vector Search Project

Once you've scaffolded your project with Copier, follow these steps to run it.

---

## ✅ Prerequisites

- Docker + Docker Compose
- (Optional) `uv` if running locally without Docker

---

## 🐳 Run with Docker (Recommended)

```bash
docker-compose up --build
```

This will:
- Start the PostgreSQL database
- Launch the FastAPI server at `http://localhost:8000`

---

## 🔌 API Usage

### ➕ Add a Vector
```bash
curl -X POST http://localhost:8000/add \
  -H "Content-Type: application/json" \
  -d '{"text": "The quick brown fox jumps"}'
```

### 🔍 Query Vectors
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"text": "brown fox"}'
```

---

## 🧪 Run Without Docker (Local Dev)

```bash
uv pip install -r requirements.txt
uvicorn app.main:app --reload
```

Ensure PostgreSQL is running and accessible on `localhost:5432`.

---

## 📄 API Docs

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)