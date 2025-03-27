from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

#choose model
model_1 = ChatOpenAI()
model_2 = ChatOpenAI()

#design prompts and parse

prompt_1=PromptTemplate(
    template='generate short and brief notes in layman terms from the text \n {text}',
    input_variables=['text'],
)
prompt_2=PromptTemplate(
    template='generate 10 Multiple choice quiz questions  (combinations of easy and hard) with answers from the text \n {text}',
    input_variables={'text'}
)
prompt_3=PromptTemplate(
    template='Merge the provided quiz and notes from into single document \n notes : {notes} and quiz : {quiz} ',
    input_variables={'notes', 'quiz'}
)
parser = StrOutputParser()

#create parallel chain using runnable , a merge chain and a final chain
notes_chain = prompt_1 | model_1 | parser
quiz_chain = prompt_2 | model_2 | parser

parallel_chain = RunnableParallel(notes=notes_chain, quiz= quiz_chain)

merge_chain = prompt_3 | model_1 | parser

final_chain = parallel_chain | merge_chain

#give text and invoke chain

text="""GPT-4o is a multimodal model trained on both text and image data, allowing it to understand visual aesthetics, styles, and compositions. Unlike previous models where image generation was separate (e.g., DALL·E 3), GPT-4o integrates image generation directly into the ChatGPT interface.

Diffusion-based generation is likely used, where noise is progressively removed from an initial random image to generate a refined output. The model learns patterns from large datasets of images but does not directly copy specific copyrighted works. Instead, it can generate images inspired by common elements of a given style, such as vibrant colors, soft lighting, and expressive characters typical of Studio Ghibli films.

To generate Studio Ghibli-style images, users can craft detailed prompts describing the scene, character, lighting, and color palette. The model interprets these textual descriptions and translates them into visual outputs.

Fine-tuned prompts can specify elements like "anime-style background," "soft pastel shading," or "hand-drawn cel-shading" to guide the model toward a Ghibli-inspired look. Iterative refinement allows users to modify generated images, adjusting aspects like facial features, colors, and expressions, improving over earlier models that lacked such control.

OpenAI has placed restrictions on directly replicating the exact styles of specific studios, including Studio Ghibli, to prevent copyright infringement. Instead, the model generates “inspired” images based on general artistic themes without replicating copyrighted characters or exact designs. OpenAI monitors the system's outputs to prevent misuse while still enabling creative expression.

Faster generation is achieved with lower latency compared to DALL·E 3 due to optimizations in rendering pipelines. The token and image processing efficiency improvements allow GPT-4o to process image and text inputs more fluidly, enabling seamless multimodal interactions.

OpenAI may introduce fine-tuning options for personalizing image outputs within ethical limits. Advanced inpainting (editing parts of images) could allow users to modify specific elements in generated images without recreating the entire output. Further improvements in consistency across multiple generations could enable better storytelling applications where characters remain visually coherent across different images.

GPT-4o's image generation technology represents a significant step forward in multimodal AI, balancing creative freedom with ethical constraints. While it enables users to generate Ghibli-inspired images, OpenAI has taken measures to prevent direct style replication to respect intellectual property laws. The model’s ability to seamlessly merge text and image generation enhances creative workflows and sets the stage for even more sophisticated AI-generated art in the future."""

res=final_chain.invoke({'text':text})

print (res)
final_chain.get_graph().print_ascii()