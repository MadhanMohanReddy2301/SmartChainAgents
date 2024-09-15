from router import llm
from langchain.schema import Document

def llm_search(state):
    """
    llm answer based on the user question

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with appended web results
    """

    print("---llm---")
    question = state["question"]

    # Wiki search
    docs = llm.invoke(question)
    #print(docs["summary"])
    llm_result = Document(page_content=docs.content)

    return {"documents": llm_result, "question": question}