"""
Download and install from:
https://ollama.com/

Then, test it in cmd, typing:
ollama --version

Copy a specific model from ollama.com. I'm gonna use llama2. So, to do this:
ollama pull llama2
To run and test it in cmd:
ollama run llama2
to finish it:
/bye
"""

# To chat with llama2 in Python terminal:

import ollama 

# Initialize the Ollama client

client = ollama.Client()

# Define the model and the input prompt
model = "llama2"
prompt = "What is the capital of USA?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)

