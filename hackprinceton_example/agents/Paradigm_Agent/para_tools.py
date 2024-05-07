ITER_SOLUTION: str = "before solving the solution, you must provide the following: solution approach (how you plan on solving the solution), post-condition (how you expect the output to be), pre-condition (how the input must be), a guess invariant (you will prove it to be a real invariant by proving that the termination condition is 'strong enough' to terminate the iterative call at the right time, if the pre-condition is weak enough to allow initial inputs)."
REC_SOLUTION: str = "before solving the solution, you must provide the following: solution approach (how you plan on solving the solution), post-condition (how you expect the output to be), pre-condition (how the input must be), an inductive hypothesis, a base case tot he inductive proof, an inductive step."
IMPERATIVE_SOLUTION: str = "Code written in 'chronological' order. Written in the way that each variable and function is defined as needed as if thought up on the spot sequentially"
PROCEDURAL_SOLUTION: str = "Divide and conquer by splitting the problem into smaller, controlled functions. These functions chain together and solve the problem."
DECLARATIVE_SOLUTION: str = "Simplifies the visual clarity of code by 'removing' all possible redundancies. Why declare variables just to pass into a function or print? You can just chain operations into function calls with no care for variables"
SOLUTION_TYPES = [ITER_SOLUTION, REC_SOLUTION, IMPERATIVE_SOLUTION, PROCEDURAL_SOLUTION, DECLARATIVE_SOLUTION]

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
load_dotenv()

@tool
def get_solution_type(solution_type: str) -> str:
    """get solution type based on iter or rec"""
    
    if (solution_type == "iter"):
        return ITER_SOLUTION
    elif (solution_type == "rec"):
        return REC_SOLUTION
    elif (solution_type == "imperative"):
        return IMPERATIVE_SOLUTION
    elif (solution_type == "procedural"):
        return PROCEDURAL_SOLUTION
    elif (solution_type == "declarative"):
        return DECLARATIVE_SOLUTION
    else:
        return ""

tools = [get_solution_type]