from openai import OpenAI

client = OpenAI(api_key="sk-proj-leT3BlbkFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print("Math Tutor Chatbot - Type 'exit' to quit")
print("==========================================")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor. Explain math problems step by step in simple English. Always show your working."},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    print(f"Tutor: {answer}\n")
