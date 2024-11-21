MODEL = "phi3:mini"

TEMPLATE = """
You are tasked with extracting specific information from the following html content:

```{webpage_data}```

please follow these instructions carefully:

1. **Extract Information:** Only extract the information that directly mathces the provided description:

```{question}```


2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.
3. **Empty Response:** If no information matches the description, return an empty string ('').
4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
"""