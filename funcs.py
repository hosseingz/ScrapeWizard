from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter


import requests

from conf import MODEL, TEMPLATE

parser = StrOutputParser()
embedding = OllamaEmbeddings(model=MODEL)
model = Ollama(model=MODEL)

prompt = PromptTemplate.from_template(TEMPLATE)



def fetch_webpage(url: str):
    try:
        html2text = Html2TextTransformer()
        loader = AsyncHtmlLoader(url)
        
        pages = loader.load_and_split()
        pages = html2text.transform_documents(pages)
        
        vectorstore = DocArrayInMemorySearch.from_documents(pages, embedding=embedding)
        
        return True, vectorstore, None
    
    except requests.exceptions.RequestException as e:
        return False, None , f"Error fetching webpage: {e}"
    except Exception as e:
        return False, None , f"An error occurred: {e}"
   


def ask_ai(question:str, vectorstore:DocArrayInMemorySearch):
    
    retriever = vectorstore.as_retriever()
    
    chain = (
    {
        'context': itemgetter('question') | retriever,
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