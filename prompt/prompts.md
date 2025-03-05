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

**Code Snippets and modifications**
-Code without chat history passed to model
<img width="256" alt="image" src="https://github.com/user-attachments/assets/bae8b55d-f582-42dd-ab01-6264bc72cbd0" />
-Output > <img width="727" alt="image" src="https://github.com/user-attachments/assets/49594031-0ba1-418c-814e-3c9ddf365f8f" />
-Output after using chat_history: <img width="722" alt="image" src="https://github.com/user-attachments/assets/0592c5e9-3bd9-43e7-bbe7-e55bff384041" />
-*All messages as it is who sent what no information-will be difficult for llm if particular message was by user or llm-create error*
-#therefore when maintaining a caht history>store all the messages awa who sent that message> maintain a dictionary user and a#
-*NO NEED OF MAINTAINING DICTIONARY > SOLVED BY LANGCHAIN LIBRARY -BUIT IN CLASSES*

**#Messages in Langchain**(refer messages.py file)
1.) System messages
2.) Human Message
3.) AI Message


