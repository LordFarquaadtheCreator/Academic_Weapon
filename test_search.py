from langchain_functions.agents.internetSearch import searchOrNot
import time

start = time.time()
print(searchOrNot('What is the weather like today in Brooklyn? Tell me in F'))
end = time.time() - start
print(end)