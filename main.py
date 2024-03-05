import chromadb
import openai
from openai import OpenAI
import os

chroma_client = chromadb.Client()

# Define the text file path
text_file_path = '/content/example.txt'  # Replace with your text file path

# Read all lines from the text file
with open(text_file_path, 'r') as file:
    documents = [line.strip() for line in file if line.strip()]  # This also skips any empty lines

# Generate IDs for each document
ids = [str(i) for i in range(len(documents))]

# Generate metadata for each document
metadatas = [{"type": "support"} for _ in range(len(documents))]

collection = chroma_client.create_collection(name="my_collection")

# Proceed with adding to the collection
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
)
