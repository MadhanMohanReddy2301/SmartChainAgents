from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain.schema import Document


## Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

def arxiv_search(state):
    """
    arxiv search based on the re-phrased question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with appended web results
    """

    print("---arxiv---")
    print("---HELLO--")
    question = state["question"]
    print(question)

    # Wiki search
    docs = arxiv.invoke({"query": "tell me about llm agent"})
    #print(docs["summary"])
    arxiv_res = docs
    print(arxiv_res)
    arxiv_res = Document(page_content=arxiv_res)
    

    return {"documents": arxiv_res, "question": question}