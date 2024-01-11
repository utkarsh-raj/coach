from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_community.vectorstores import Chroma

embeddings_model = OpenAIEmbeddings()

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
loader = WebBaseLoader("https://en.wikipedia.org/wiki/The_Office_(American_TV_series)")
raw_documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = Chroma.from_documents(documents, OpenAIEmbeddings())

# query = "How did Mark Harris review the second season of the show?"
query = "Write a five question quiz on the show with four option and the right answer. Keep the questions strictly about the show"
# docs = db.similarity_search(query)
# print(docs[0].page_content)

embedding_vector = OpenAIEmbeddings().embed_query(query)
docs = db.similarity_search_by_vector(embedding_vector)
# print(docs[0].page_content)


prompt_template = PromptTemplate.from_template(
    "Answer the given query using only the context provide in the context tags below\n<context>{context}</context>\nQuery:{query}"
)
llm = OpenAI()

prompt = prompt_template.format(context=docs[0].page_content, query=query)
# print(prompt)
res = llm.invoke(prompt)
print(res)