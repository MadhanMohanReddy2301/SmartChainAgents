# LLM Agent Routing System

This project is an intelligent routing system for user queries, using the LangChain framework and Groq's Gemma2-9b-It model. It allows queries to be directed to the most relevant data source — either **arxiv_search** (for AI research papers), **Wikipedia** (for human-related information), or an **LLM** (for general queries).

## Features

- **Context-Aware Routing**: Routes user queries based on the context to either arxiv, Wikipedia, or an LLM.
- **Flexible Query Handling**: Supports different types of user queries related to AI research, human information, or general knowledge.
- **Powered by LLM**: Utilizes Groq's Gemma2-9b-It model for intelligent query understanding and routing.

## Project Components

1. **LangChain**: Used for building the agent that handles the query routing process.
2. **Groq's Gemma2-9b-It Model**: The large language model used to interpret user queries and generate structured output.
3. **arxiv_search**: Searches for AI-related research papers.
4. **Wikipedia Search**: Handles queries related to human knowledge.
5. **LLM Search**: A fallback option for general queries that don’t fit into the other categories.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MadhanMohanReddy2301/SmartChainAgents.git
    ```

2. Navigate to the project directory:
    ```bash
    cd SmartChainAgents
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by adding your Groq API key:
    ```bash
    export GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. Initialize the LLM router system by running the script:
    ```bash
    python graph.py
    ```

2. Test the routing functionality with some example queries:
    ```python
    question_router.invoke({"question": "Who is Shahrukh Khan?"})
    question_router.invoke({"question": "What are the types of agent memory?"})
    ```

3. The system will route the query to the appropriate source and return the result accordingly.

## Example

```python
# Example query for Wikipedia search
{
  "datasource": "wiki_search"
}

# Example query for arxiv search
{
  "datasource": "arxiv_search"
}

