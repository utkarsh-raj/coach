from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} {art_form} about {subject}"
)
llm = OpenAI()

prompt = prompt_template.format(adjective="funny", art_form="joke", subject="trekkers")
print(prompt)
res = llm.invoke(prompt)
print(res)

