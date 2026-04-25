from transformers import pipeline

generator = pipeline(
    "text2text-generation",  
    model="google/flan-t5-base",
    max_new_tokens=150,
    do_sample=False
)

def generate_answer(query, docs):
    context = "\n".join([d["text"] for d in docs])

    prompt = f"""
Context:
{context}

Question: {query}

Give a short and clear answer using only the context.
Do NOT repeat the question or the context.

Answer:
"""

    response = generator(prompt)[0]["generated_text"]
    answer = response.split("Answer:")[-1].strip()

    return answer