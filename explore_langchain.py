from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

llm = ChatOpenAI()

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class travel influencer."),
#     ("user", "{input}")
# ])



# output_parser = StrOutputParser()

# chain = prompt | llm | output_parser

# r = chain.invoke({"input": "What are the best destinations to travel in Europe?"})
# print(r)

loader = WebBaseLoader("https://en.wikipedia.org/wiki/The_Office_(American_TV_series)")

docs = loader.load()

embeddings = OpenAIEmbeddings()
print(docs)

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

