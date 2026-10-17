# LLM & RAG Lab

Hands-on experiments with **Large Language Models**, **LangChain**, **Retrieval-Augmented Generation (RAG)** and **LangGraph agents**.

This repository documents my learning process: I rebuild the core concepts from scratch while studying a LangChain/RAG course, then extend each topic with my own experiments (different documents, prompts, models and parameters).

> Goal: combine LLMs with my background in **Computer Vision** — e.g. asking natural-language questions about real-time object detection results.

## Topics

| # | Topic | Status |
|---|-------|-------|
| 01 | LLM basics & API usage | 🔄 |
| 02 | Prompt templates & chains | ⏳ |
| 03 | Memory & chat history | ⏳ |
| 04 | Document loaders, text splitting & embeddings | ⏳ |
| 05 | RAG pipeline with a vector store | ⏳ |
| 06 | Advanced RAG (re-ranking, hybrid search) | ⏳ |
| 07 | Agents with LangGraph | ⏳ |
| 08 | Mini projects | ⏳ |

✅ done · 🔄 in progress · ⏳ planned

## Structure

Each folder contains:
- `notes.md` — what I learned, in my own words
- notebooks / scripts — my implementation
- `my_experiment` — my own variation on the topic

## Setup

```bash
git clone https://github.com/esra-yasar/llm-rag-lab.git
cd llm-rag-lab
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env       # then add your own API key
```

## Tech
  Python · LangChain · LangGraph · Claude / OpenAI / Gemini APIs · LangSmith · FAISS / Chroma · Jupyter