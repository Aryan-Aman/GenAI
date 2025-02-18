**Models**: -Core interfaces through which we interact with AI models.

**Problem**: *Different llm api providers >different codes> suppose i have to use 2 different models in my app so have to write different codes eg openAI and Claude 
         both will have diferent code.And responses also different of different APIs.*
**Solution**:Langchain > *an interface through which we can use any LLM API in standardized fashion. Not much changes in code.*

Two types of AI models for communicate in langchain:

![langchainModels](https://github.com/user-attachments/assets/4a18db1a-6d28-481a-95ae-c835491b7275)

**Open Source Models**
-freely available, can be downloaded modified, fine-tuned, and deployed without restrictions from a central provider.
-full control and customization
-can be deployed on premise or cloud
eg: llama, deepseek,mistral,falcon
#Where to find ?- Huggingface(largest open source models repo)
![Alt Text](images/openmodels.png)

Disadvantages
**Commercial/Closed source Models**
- model on companys server, can be interacted via models API > cost of using api.
