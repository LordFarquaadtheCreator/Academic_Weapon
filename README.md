## Have you ever had a class so difficult that not even the textbook helped you understand the concepts? 
## Did you ever wonder if there was some resource out there that could break down concepts using the same niche textbook that your professor uses?

## If you said yes to either of these Questions, meet:

## Academic Weapon


<details>
<summary> How does it work? </summary>
just testing it right now 1
<br> im just testing it right now 2
</details>
# Caution!!!
- inputs over 512 chars MUST be sent in batches 

## How the RAG Works
- file `chroma.py` contains all vector database related functions
- it vectories all inputs, queries it against the database and returns `n` relevant data points (max 512 chars)
- this data is sent to GPT to be included as context for the user's prompt


