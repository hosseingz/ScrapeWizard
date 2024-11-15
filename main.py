import streamlit as st
from funcs import *



st.title("Welcome")
st.write('This is an AI web scraper designed to assist you in extracting valuable information from websites effortlessly.')

st.write("""
Our AI-powered web scraper allows you to input any URL and specify exactly what content you're interested in extracting from that page.

### Key Features:
- **Flexible Input**: Enter any valid URL and specify your requirements through a customizable prompt.
- **User-Friendly Interface**: Enjoy an intuitive design that makes it easy for anyone to use the web scraper.
- **AI Integration**: Leverage the power of artificial intelligence to extract relevant information accurately.

### How It Works:
1. **Input URL**: Start by entering the URL of the website you wish to scrape.
2. **Define Your Request**: In the prompt section, explain what specific information you would like to retrieve. Be as detailed as possible to get the best results.
3. **Start the Scraping Process**: Click the "search" button, and the AI will handle the rest, pulling the desired data from the provided URL.

### Getting Started:
To contribute, report issues, or explore the source code, please visit our project's GitHub repository: [GitHub - Scrape Wizard](https://github.com/hosseingz/ScrapeWizard)

We are continually improving this project and welcome contributions from the community. Happy scraping!
""")


url = st.text_input("URL", placeholder='Enter the URL you want to scrape')

if prompt := st.chat_input("What do you want from this URL?"):

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Generating response...'):
        
        status, webpage_data = fetch_webpage(url)
    
        if status:

            user_prompt = f"""
You are tasked with extracting specific information from the following html content:

```{webpage_data}```

please follow these instructions carefully:

1. **Extract Information:** Only extract the information that directly mathces the provided description:

```{prompt}```


2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.
3. **Empty Response:** If no information matches the description, return an empty string ('').
4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
"""
                      
            response = ask_ai(user_prompt)
            st.write_stream(stream_parser(response))

        else:
            st.error(f'Error: {webpage_data}')
