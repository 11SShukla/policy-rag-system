from app.rag_pipeline import ask

question = "What are RBI KYC requirements?"

answer = ask(question)

print("\nAnswer:\n")
print(answer)