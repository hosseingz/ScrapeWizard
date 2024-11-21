MODEL = "phi3:mini"

TEMPLATE = """
Please provide a direct answer to the question based on the context below:

Context: {context}

Question: {question}

Instructions:

1. Extract Relevant Information: Identify and extract only the information that directly answers the question. Focus specifically on details from the context that match the query.

2. Avoid Extraneous Content: Do not include any additional explanations, comments, or surrounding narrative. Your response should be concise and to the point.

3. Return Empty if No Match: If there is no relevant information that answers the question, respond with an empty string ('').

4. Output Format: Ensure your response includes only the requested data without any additional text or formatting.

4. Direct Data Only: Your output should contain only the data that is explicitly requested, with no other text.
"""