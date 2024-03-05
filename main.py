import chromadb
import openai
from openai import OpenAI
import os
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

# Set the API keys

os.environ["OPENAI_API_KEY"] = #your openai API key goes here
os.environ['SERPAPI_API_KEY'] = #your SERPAPI API key goes here


client = OpenAI()
chroma_client = chromadb.Client()

# Define the text file path
text_file_path = '/CRAG/example.txt'  # Replace with your text file path

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

#initialize serp api
tool_names = ["serpapi"]
tools = load_tools(tool_names)
agent = initialize_agent(tools, client, agent="zero-shot-react-description", verbose=True)

#this will be the user's question
query = "when was messi born?"

#get the retrieval based on the query
results = collection.query(
    query_texts=query,
    n_results=1
)

eval_prompt = """ User's query: {query}
information extracted: {results}
""".format(query=query, results=results)

evaluator = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "Analyze the information extracted from the provided document in relation to the specific user query. Determine the relevance and adequacy of the extracted data in addressing the user's question. If the extracted data directly provides a clear answer to the user's query, respond with 'Correct'. If the information is related but does not definitively answer the user's query, or if there's uncertainty about its relevance, respond with 'Ambiguous'. In the event that the extracted data fails to address the user's query at all, and seems entirely unrelated, respond with 'Incorrect'."},
    {"role": "user", "content": f'{eval_prompt}'}
  ]
)

if x == "Correct":
    # Do something if x is correct
    refinement = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "refine the information extracted to directly address the user's query, eliminating any irrelevant details and retaining only the pertinent information that responds to the query."},
    {"role": "user", "content": f'{eval_prompt}'}
  ]
)
    print(refinement.choices[0].message.content)
elif x == "ambiguous":
    refinement = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "refine the information extracted to directly address the user's query, eliminating any irrelevant details and retaining only the pertinent information that responds to the query."},
    {"role": "user", "content": f'{eval_prompt}'}
  ]
)
    search = agent.run(query)
    combined_result = refinement + search

else:
    search = agent.run(query)
