from langgraph.graph import END, StateGraph, START
from arxivagent import arxiv_search
from edges import route_question
from llmagent import llm_search
from wikiagent import wiki_search
from graphstate import GraphState
from pprint import pprint

workflow = StateGraph(GraphState)
# Define the nodes
workflow.add_node("wiki_search", wiki_search)  # web search
workflow.add_node("arxiv_search", arxiv_search)  
workflow.add_node("llm_search", llm_search)

# Build graph
workflow.add_conditional_edges(
    START,
    route_question,
    {
        "wiki_search": "wiki_search",
        "arxiv_search": "arxiv_search",
        "llm_search": "llm_search",
    },
)
workflow.add_edge( "arxiv_search", END)
workflow.add_edge( "wiki_search", END)
workflow.add_edge("llm_search", END)
# Compile
app = workflow.compile()

from IPython.display import Image, display

try:
    # Get the image as a PNG from the graph and save it to a file
    img_data = app.get_graph().draw_mermaid_png()

    # Save the image to a file
    with open("graph_image.png", "wb") as f:
        f.write(img_data)

    # Optionally display the image in the notebook or script
    display(Image(img_data))

except Exception as e:
    # Print the exception if something goes wrong
    print(f"An error occurred: {e}")




# Run
inputs = {
    "question": "write 100 words about india"
}
for output in app.stream(inputs):
    for key, value in output.items():
        # Node
        pprint(f"Node '{key}':")
        # Optional: print full state at each node
        # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
    pprint("\n---\n")

# Final generation
pprint(value["documents"].page_content)