from langchain_core.prompts import PromptTemplate


#building template
template=PromptTemplate(
    template="""Please summarize the research paper titled "{select_paper}" with following specifications:
        Explanation style :{input_style}
        Explanation length : {input_length}
        Ensure the summary is clear, alligned with  the provided style and length and retains key insights from the paper.
        If certain information is not available in the paper, state that explicitly and provide relevant context where possible instead of guessing. 
        Here are the definitions of summary styles: 
        1. Mathematical Details :
            -Focus on mathematical formulations, equations if pre sent in the paper. 
            -Include key formulas, derivations, and mathematical proofs when relevant.
        2. Code-oriented: 
            -Provide implementation details, pseudocode, or real code snippets in Python or relevant programming languages.
            -Focus on algorithmic structure and computational considerations. 
        3. Beginner-Friendly: 
            -Explain concepts in a simple, easy-to-understand manner, avoiding heavy jargon. Use analogies or everyday examples where possible. 
        4. Technical:
            -Use domain-specific terminology and detailed explanations. 
            -Assume the reader has prior knowledge in the field. 
            -Provide in-depth theoretical or experimental analysis. 
        5. Comprehensive:
            -Cover all aspects, including background, methodology, key findings, and implications. 
            -Aim for completeness with structured explanations.
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
        Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
        input_variables=['select_paper', 'input_style','input_length'],
        validate_template=True
    )
template.save("template.json")