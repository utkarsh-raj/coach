import chromadb
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.HttpClient(host='localhost', port=8000)

collection = client.get_or_create_collection(name="test_collection", embedding_function=default_ef)

print(collection)

collection.add(
    documents=[
        "Ghostfreak, an alien with invisibility and intangibility powers, is one of the spooky additions to Ben 10's arsenal.",
        "One of Ben 10's iconic aliens is Heatblast, known for his ability to generate and control fire.",
        "XLR8 is another fast and agile alien form of Ben 10, allowing him to move at incredible speeds.",
        "Upgrade is a technologically advanced alien that can merge with and enhance any technology it comes into contact with.", 
        "Wildmutt, a feral and beastly alien with enhanced senses, is one of Ben 10's formidable transformations."
    ],
    metadatas=[
        {"alien": "Ghostfreak", "abilities": '["Invisibility", "Intangibility"]'},
        {"alien": "Heatblast", "abilities": '["Fire Generation", "Fire Control"]'},
        {"alien": "XLR8", "abilities": '["Super Speed", "Agility"]'},
        {"alien": "Upgrade", "abilities": '["Technological Enhancement"]'},
        {"alien": "Wildmutt", "abilities": '["Enhanced Senses"]'}
    ],
    ids=["ghostfreak", "heatblast", "xlr8", "upgrade", "wildmutt"]
)

print(collection.peek()) # returns a list of the first 10 items in the collection
print(collection.count()) # returns the number of items in the collection