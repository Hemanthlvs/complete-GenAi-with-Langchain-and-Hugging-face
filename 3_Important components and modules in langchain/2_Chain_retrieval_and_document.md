## 🔗 What is a Chain in RAG?

In **LangChain**, a **chain** means step-by-step processing. In **RAG (Retrieval-Augmented Generation)**, chain connects two main steps:

1. **Retrieval** – Find useful documents based on the question
2. **Generation** – Give those documents to LLM to generate an answer

---

## 🔍 What is Retrieval Chain?

- Only fetches relevant documents
- No answer generation
- Example: Using `chroma_db.as_retriever()` to get matching docs

---

## 🧾 What is Document Chain (QA Chain)?

- Takes retrieved documents + your question
- Feeds them to the LLM
- Returns the final answer
- Example: Using `load_qa_chain(llm, chain_type="stuff")`

---

## ✅ Simple Summary

| Chain Type         | Work it does                   |
|--------------------|--------------------------------|
| Retrieval Chain     | Brings matching documents      |
| Document Chain (QA) | Creates answer using LLM       |
| RAG Chain           | Combo of both above steps      |

---

## 🔁 Full Flow Example

```python
retriever = chroma_db.as_retriever()
docs = retriever.get_relevant_documents("Your question")

qa_chain = load_qa_chain(llm, chain_type="stuff")
answer = qa_chain.run(input_documents=docs, question="Your question")
print(answer)





📄 Your Question
      │
      ▼
🔍 Retrieval Chain (Retriever)
 - Finds related documents from Vector DB (like Chroma)
      │
      ▼
📚 Retrieved Documents
      +
❓ Original Question
      │
      ▼
🧠 Generation (Document Chain / QA Chain)
 - Sends docs + question to LLM
 - LLM generates a smart answer
      │
      ▼
✅ Final Answer
