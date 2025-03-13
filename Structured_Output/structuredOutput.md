![structuredOutput drawio](https://github.com/user-attachments/assets/8a0dd1bf-8501-4ef4-a457-3223bcc9f068)
![strOP2](https://github.com/user-attachments/assets/7b33b342-f195-4755-9940-daf70f62af8a)
![strdOP3](https://github.com/user-attachments/assets/a478f67e-44ec-42a0-8a3b-15ab997c5ab0)






**Need ?**
-Data Extraction ( eg. nukri.com>resume uploaded> Extract all text like name,college,10th,12th etc. store into database > send to llm>get data in json format>store in DB via code )
- API building (eg. Amazon Review >via API  extract all review topics for diff. products,overall sentiment etc )
- Agents [chatbots on steroids] (eg. calculator agent > prompt-tell sqrt of 2 - text cant be given to calc. as its expecting numbers -  run str output on prompt and fetch numbers - 2 and sqrt - will give output)

**Ways to get Structured Output**-

*with_structured_output*: before calling model_invoke() we call this function and give the data format > data format specify 2/3 ways : Typed Dict; Pydantic; JSON Schema
1.) Typed Dictionary : In python we just create onthe go dict. > person = {"name" : "aman", "age" : 35}, Issue : suppose 2 progrmrs working on same projct /file and he treats age as string instead of no. so issue in runtime.
              <ins>Solun : define first how the dict will look like > create class  person and in that dict name key , age key : will have string and int as values respectively. > tells Py what keys are required & what types of values they should have</ins>
              <ins>Drawback :  If let age is int even then we can keep age value as string.>code will run > NO Validation</ins>
               

!!Problem Statement > Reviews of phone > send to llm > o/p should be structured (dict).keys>summary and sentiment 