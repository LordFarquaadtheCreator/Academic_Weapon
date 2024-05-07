template_prompt = """

You need to answer the question in the proper format. The proper format is decided by
the type of problem that the question is asking. You can use the following tools to help you:

{tools}

With the inputs being iter for iterative, rec for recursive, imperative for imperative, procedural for procedural, and declarative for declarative.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of {tool_names}
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""