### Edges ###
from router import question_router

def route_question(state):
    """
    Route question to wiki search or arxiv.

    Args:
        state (dict): The current graph state

    Returns:
        str: Next node to call
    """

    print("---ROUTE QUESTION---")
    question = state["question"]
    source = question_router.invoke({"question": question})
    if source.datasource == "wiki_search":
        print("---ROUTE QUESTION TO Wiki SEARCH---")
        return "wiki_search"
    elif source.datasource == "arxiv_search":
        print("---ROUTE QUESTION TO arxiv_search---")
        return "arxiv_search"
    elif source.datasource == "llm_search":
        print("---ROUTE QUESTION TO llm_search---")
        return "llm_search"
