from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter

from bs4 import BeautifulSoup
import requests

from .conf import MODEL, TEMPLATE

parser = StrOutputParser()
embedding = OllamaEmbeddings(model=MODEL)
model = Ollama(model=MODEL)

prompt = PromptTemplate.from_template(TEMPLATE)



def fetch_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.find('title').text
        
        # Extract meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            meta_description = meta_description.get('content')
        else:
            meta_description = ''
        
        # Extract headings
        headings = [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        
        # Extract paragraphs
        paragraphs = [p.text for p in soup.find_all('p')]
        
        # Combine data into a single string
        data = f"Title: {title}\nMeta Description: {meta_description}\nHeadings: {', '.join(headings)}\nParagraphs: {' '.join(paragraphs)}"
        
        # Load data into vector store
        vectorstore = DocArrayInMemorySearch.from_documents([data], embedding=embedding)
        
        return True, vectorstore

    except requests.exceptions.HTTPError as http_err:
        return False, f"HTTP error occurred: {http_err}"  # HTTP error
    except requests.exceptions.ConnectionError as conn_err:
        return False, f"Connection error occurred: {conn_err}"  # Connection error
    except requests.exceptions.Timeout as timeout_err:
        return False, f"Timeout error occurred: {timeout_err}"  # Timeout error
    except requests.exceptions.RequestException as req_err:
        return False, f"An error occurred: {req_err}"  # Other errors
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"  # Unexpected error



def ask_ai(question:str, vectorstore:DocArrayInMemorySearch):
    
    retriever = vectorstore.as_retriever()
    
    chain = (
    {
        'context': itemgetter('question') | retriever, # بنا به چیزی که میخوایم توی پی دی اف سرچ میشه و بعنوان کانتکست به پرامپت فرستاده میشه
        'question': itemgetter('question')
    }
        | prompt
        | model
        | parser
    )
    
    return chain.stream({'question': question})
        


def stream_parser(stream):
    for chunk in stream:
        yield chunk