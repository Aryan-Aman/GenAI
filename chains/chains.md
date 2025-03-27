Chains
=========
-can create pipeline for small steps in LLMs by connecting them and forming pipeline.
-1st step output is input for next step and so On.
-to give input to only 1st step and trigger pipeline.
-can create different structured pipelines like Linear/sequential pipeline, Parallel processing, conditional chains etc.
- | : is pipe operatorand the process of using it to add components is called LCEL (langchain expression language)
-can visualize chains by printing it using funtion get_graph().print_ascii() [install grandalf]
![alt text](image.png)