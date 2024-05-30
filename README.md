### Have you ever had a class so difficult that not even the textbook helped you understand the concepts? 
### Did you ever wonder if there was some resource out there that could break down concepts using the same niche textbook that your professor uses?

### If you said yes to either of these Questions, meet:

# Academic Weapon


<details>
<summary>What does it do? </summary>
Academic Weapon allows users/students to upload their specific class resources such as textbooks, previous homeworks, and even previous exams so that our AI Application can parse through all of the information, vectorize it, and then assist the user. If the question is out of the scope of the vectorized resources, our AI can also web scrape using the BING API in order to gather additional information.
 <br>
 <br>
  # Uses 
<br>
  - Can answer questions such as "what is an eigen vector?"<br>
  - Can create and solve practice problems with the user<br>
  - Can teach topics from the textbook or even out of the scope of the textbook using web scraping!<br>
<br>

</details>

<br>

<details>
<summary>How does it work? </summary>
## Visualization:

![Visualization](Untitled (1).png)


# THEY NOT LIKE US 
![Our team for real](https://tenor.com/view/kendrick-lamar-god-is-gangsta-u-ahhh-scream-gif-6349874768192364613.gif)

- file `chroma.py` contains all vector database related functions
- it vectories all inputs, queries it against the database and returns `n` relevant data points (max 512 chars)
- this data is sent to GPT to be included as context for the user's prompt
</details>
<br>
<br>
<summary> How to run it on your computer? </summary>
### Make sure your computer has these minimum requirements<br>
<li> Atleast 8 Gigs of Ram, preferrably 16 <br>
<li> Python 3.10<br>
<li> An open mind!<br>
<br>
### Now to run it, you have to 
 1. Fork the repo onto your computer<br>
 2. Open up a virtual environment <br>
 3. ```pip install -r requirements.txt```<br>
 4. ```python llama.py```<br>

</details>

# Caution!!!
- inputs over 512 chars MUST be sent in batches 




