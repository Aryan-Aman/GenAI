from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_history=[
    SystemMessage(content="You are a helpful chatbot assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input =="exit":
        print("Exited successfuly")
        break
    response=model.invoke(chat_history)#invoke func is flexible to get single message awa list of messages
    chat_history.append(AIMessage(response.content))
    print("bot :",response.content)
print(chat_history)