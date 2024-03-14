# Academic_Weapon
The Academic Weapon will respond to your specific academic needs by querying relevant endpoints and using pre-defined functions.

# Caution!!!
- inputs over 512 chars MUST be sent in batches 

## How the RAG Works
- file `chroma.py` contains all vector database related functions
- it vectories all inputs, queries it against the database and returns `n` relevant data points (max 512 chars)
- this data is sent to GPT to be included as context for the user's prompt