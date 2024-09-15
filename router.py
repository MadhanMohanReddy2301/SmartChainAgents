### Router

from typing import Literal
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

import os

# Data model
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["arxiv_search", "wiki_search", "llm_search"] = Field(
        ...,
        description="Given a user question choose to route it to wikipedia or arxiv_search or llm_search.",
    )

# LLM with function call
from langchain_groq import ChatGroq
import os
groq_api_key=os.getenv('GROQ_API_KEY')
os.environ["GROQ_API_KEY"]=groq_api_key
llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma2-9b-It")
structured_llm_router = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are an expert at routing a user question to a arxiv_search or wikipedia or llm_search.
The arxiv_search contains documents related to research papers about ai agents and LLMS.
Use the wikipedia for questions on the human related infomation. Otherwise, use llm_search."""


route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router
"""print(
    question_router.invoke(
        {"question": "who is Sharukh Khan?"}
    )
)
print(question_router.invoke({"question": "What are the types of agent memory?"}))"""