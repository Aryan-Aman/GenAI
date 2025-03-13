from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini")

#schema
class strdOutput(TypedDict):
    summary : str
    sentiment : str

strd_output=model.with_structured_output(strdOutput)

res=strd_output.invoke("""This phone is great in many aspects but has some flaws. The design is sleek and premium, and the performance is smooth for daily tasks and gaming. The camera is good but struggles in low light. The battery life is decent but could be better with heavy usage. The biggest downside is the slow charging speed, which can be frustrating. Overall, it’s a solid phone with minor drawbacks, but for the price, it's still a good choice.""")
print(res)