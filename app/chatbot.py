from app.rag_pipeline import ask

print("Policy RAG Assistant Ready")
print("Type 'exit' to quit\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask(question)

    print("\nAssistant:\n", answer)