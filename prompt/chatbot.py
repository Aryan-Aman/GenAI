from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_history=[]

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input =="exit":
        print("Exited successfuly")
        break
    response=model.invoke(chat_history)#invoke func is flexible to get single message awa list of messages
    chat_history.append(response.content)
    print("bot :",response.content)
print(chat_history)