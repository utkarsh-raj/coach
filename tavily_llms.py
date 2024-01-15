from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

tool = TavilySearchResults()

# res = tool.invoke({"query": "What is the price of Silver in India on 14 January 2024"})
res = [{'url': 'https://www.91mobiles.com/finance/silver-rate-in-india', 'content': "Silver Rate Today in India (14th Jan 2024)  10 Gram, 100 Gram & 1 kg Silver Prices in India Today Silver Price For Last 10 Days in India  Silver Price History in India Compare Silver vs Gold Performance Monthly Silver Price Movement  Silver Rate Today in Major Cities in India Things to Know Silver Weight Converter Silver Price in your City FAQLast Updated: 10th Jan 2024. If you're looking to invest in silver or to buy silver jewellery for personal use, find here all vital information you may need before going ahead with your purchase. Find here the latest prices for Silver in India and also compare them to make an informed decision. Silver rate in India today is ₹718 per 10 grams ..."}, {'url': 'https://www.livemint.com/market/commodities/gold-and-silver-prices-today-on-14-01-2024-check-latest-rates-in-your-city-11705207508499.html', 'content': 'Gold and silver prices Today on 14-01-2024 : Check latest rates in your city  Gold And Silver Prices Today: 10 gm of 24 carat gold was at Rs.63970.0 in Delhi whereas 1 kg of silver was Rs.76000.0  The cost of silver is Rs.76000.0 per kg. Gold and Silver prices in your city are as follows:  Chennai has gold price of Rs.64530.0/10g and silver price of Rs.77500.0/1kg.Livemint Gold And Silver Prices Today: 10 gm of 24 carat gold was at Rs.63970. in Delhi whereas 1 kg of silver was Rs.76000. in Delhi. Gold and Silver price today Gold And Silver...'}, {'url': 'https://www.financialexpress.com/silver-rate-today/', 'content': "The Financial Express Silver Rate Today in India (Sunday, Jan 14, 2024) Today silver Price/gm in India (INR)  Silver Trading Frequently Asked Questions (FAQs) How much is one gram of silver worth today? ₹76.5  Major Cities silver Rate Today silver Rate in India for Last 10 Days (1 kg) Trending Silver Facts  In India, where can I sell my silver bullion?Silver Rate Today in India (Wednesday, Jan 10, 2024) SILVER GOLD Jan 10, 2024 SILVER Rate in Mumbai₹792 / 10 gm ₹ 17 Today silver Price/gm in India (INR) GMToday's..."}, {'url': 'https://indiadailymail.com/markets/gold-and-silver-prices-today-on-14-01-2024-check-latest-rates-in-your-city/', 'content': 'Gold and silver prices Today on 14-01-2024 : Check latest rates in your city Date: Related stories  The price of silver is Rs.76000.0 in line with kg. Gold and Silver costs for your town are as follows:  Chennai has gold value of Rs.64530.0/10g and silver value of Rs.77500.0/1kg.  Delhi has gold value of Rs.63970.0/10g and silver value of Rs.76000.0/1kg.Gold And Silver Costs As of late: Gold costs noticed a remained customary on Sunday.'}]
# print(res)
prompt_template = PromptTemplate.from_template(
    "Answer the given query using only the context provide in the context tags below\n<context>{context}</context>\nQuery:{query}"
)
llm = OpenAI()
query = "What is the price of Silver in India on 14 January 2024"

context = "\n".join([str(x["content"]) for x in res])

prompt = prompt_template.format(context=context, query=query)
print(prompt)
res = llm.invoke(prompt)
print(res)