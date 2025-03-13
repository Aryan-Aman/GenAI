from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini")

#schema
class strdOutput(TypedDict):
    key_themes : Annotated[list[str], "Write down all key themes given in the review in a list"]
    summary : Annotated[str, "A brief short summary of the review"]
    sentiment :Annotated[Literal["pos", "neg"], "Return sentiment of review either, negtive, positive or neutral"] #instead of positive negative > pos neg -> Import Literal
    pros : Annotated[Optional[list[str]], "Write down all pros inside a list"]
    pros : Annotated[Optional[list[str]], "Write down all cons inside a list"]
    name: Annotated[Optional[str], "Write only the name of the reviewer not the model"]

strd_output=model.with_structured_output(strdOutput)

res=strd_output.invoke("""I’ve been using the XYZ Pro for a while now, and it’s been a mix of impressive features and a few minor drawbacks. The 6.7-inch AMOLED display is absolutely stunning, offering vivid colors and a smooth 120Hz refresh rate, making everything from scrolling to gaming feel seamless. The Snapdragon 8 Gen 3 processor ensures fast performance with no lag, though heat buildup can be an issue during prolonged gaming sessions.
The camera system delivers excellent results in daylight, with the 50MP main sensor capturing sharp and detailed images. However, the telephoto lens struggles in low light, producing slightly grainy images. Battery life is reliable, lasting a full day with moderate use, but the charging speed is slower than expected, and the lack of a charger in the box is disappointing.
Pros:
Display: Stunning AMOLED panel with a smooth refresh rate
Performance: Fast and efficient for multitasking and gaming
Camera: Great primary camera for daylight photography
Battery: Lasts a full day on moderate use
Cons:
Heating: Noticeable heat buildup during extended gaming
Low-light camera: Telephoto lens struggles in dim lighting
Charging speed: Slower than many competitors
Accessories: No charger included in the box
            Review by Aman Aryan""")
print(res) #type > dict
print(res['summary'])
print(res['sentiment'])
print(res['name'])

#TypedDict only for representational purpose. Above problm> No gurantee summary should be a str then we get str only may be we can get other format also so for data validation use Pydantic
