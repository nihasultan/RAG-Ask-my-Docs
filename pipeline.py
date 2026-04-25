from ingestion import get_chunks
from retrieval import build_index, retrieve
from generator import generate_answer

chunks = None
index = None

def initialize():
    global chunks, index
    chunks = get_chunks()
    index, _ = build_index(chunks)

def ask(query):
    retrieved = retrieve(query, chunks, index)
    answer = generate_answer(query, retrieved)
    return answer, retrieved