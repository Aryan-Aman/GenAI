Runnables
=========

**why Exist ?**
-allow chaining different operations (like prompts, models, and parsers) seamlessly while handling parallel execution, streaming, and async processing efficiently.

**Components -> LLM applications**
-When langchain team found that AI engineers build llm apps connecting different components in diff ways > few things common like building prompts in every llm app then send it to llm.(every task). *So it was done manually but what if automate using built in function- 1 more level of abstraction- these are called chains Simple chain - llm chain* 

-Any RAG based application - retrieval is done for sure, [Retrieval: user gives query-search this in vector DB-this query related to which chunk], get relevant text from query+chunk text> build Prompt using these two and send to llm. *so what if we convert this whole task to chain build func(llm,retrieval) automatically BTS whole thing will get done  called Retrievar QA Chain*

**Problem**
-Too many chains over time for every usecase- langchain codebase became huge- which langchain to use for which usecase
-*Why too many chains?*- because components (eg llm, prompt, parsers etc) these are not standardized(dont follow same set of standards-developed independently and behaves differently)
**Solution**- Introduce a new component called *RUNNABLES*

#RUNNBALES ?
-Unit of work->give input get output
-common interface(same set of methods with same name) ->eg .invoke(), batch(), stream()
-can conect these runnables (r1)<->(r2)<->(r3)= R1
-the above workflow is itself a runnable (R1)<->(R2) Where R2 is (r4)<->(r5)
-eg visualize considering lego blocks