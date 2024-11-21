MODEL = "phi3:mini"

TEMPLATE = """
Answer the question based on the context below: 

Context : {context}


please follow these instructions carefully:

1. **Extract Information:** Only extract the information that directly mathces the provided question:

Question: {question}


2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.
3. **Empty Response:** If no information matches the question, return an empty string ('').
4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
"""