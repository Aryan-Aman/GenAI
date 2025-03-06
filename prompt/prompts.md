-*Prompts are the input/instructions/queries given to model to guide its output*
**Types**
1) Text based
2) Multimodal (images/videos/sound)

**STATIC Prompt**- User gives different input/prompt each time to get a new response from llm- not used much-bcs when user is able to write static prompt -user is getting more control. Outputs depend on prompt too much(sensitive).More chance of mistakes if we take static prompt from user
-*user should get consistent experience*

**Solution**-*use/prepare template-**dynamic prompt**

**Prompt Template**
-Structured way to create prompts dynamically by inserting variables into a predefined template
-No hardcoding of prompts
-Define placeholders that can be filled at runtime with different inputs.
-*Resuable, flexible, easy to manage, -dunamic user inputs / automated workflows*

**Q. wHY USE PROMPTTEMPLATE OVER FSTRING?**
-DEFAULT validation-*validate_template=True*
-Resuable - can use template as a json file (when template is required for multiple pages)-prompt_generator>saved as template.json
-Langchain ecosystem 

#Template.json file automatically created when after running prompt_generator.py file
#invoke is called 2 time - for prompt template and for model in response.- 2 step process>prompt designed then sending to llm 
- **use CHAIN** to call invoke only once >tie both steps to create chain template and model

![invoke](images/invoke.png)
![chat_prompt_template_argument](image.png) > ![Output](image-1.png)> wrong 
-*LangChain's ChatPromptTemplate.from_messages() expects a list of tuples (("role", "message")), not actual SystemMessage or HumanMessage objects.*


**Message Placeholder**
-in langchain is a special placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.
-eg. A customer raised a return related issue for his order, after few days again he asks for refund , chat_history.txt is a file somewhere stored in cloud db for eg. .