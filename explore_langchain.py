from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class travel influencer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

r = chain.invoke({"input": "What are the best destinations to travel in Europe?"})
print(r)

