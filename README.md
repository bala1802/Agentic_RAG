# Agentic RAG

Explored implementing the Agentic Retrieval-Augmented Generation (RAG) design pattern using LangChain, Groq, and CrewAI. This approach leverages multiple AI agents working together to enhance the efficiency and accuracy of information retrieval and generation processes.

## What is Agentic RAG?

Agentic AI systems are engineered to tackle complex problems with minimal human oversight. These systems consist of multiple agents that communicate with one another, functioning either under a centralized command or in a decentralized, self-organizing way. As businesses increasingly adopt multi-agent systems to automate intricate processes and address challenging tasks, the role of these AI-driven solutions continues to grow in importance.

## How to read this repository?

```

.
├── README.md
├── agentic_rag.ipynb
├── agents.py
├── config.py
├── crew_operations.py
├── llm_utils.py
├── prompts.py
├── rag_tool.py
├── router.py
├── tasks.py
├── tavily_utils.py

```

## Configure API Keys

### Groq

A high-performance computing platform that accelerates AI workloads, making it ideal for handling the complex computations involved in RAG systems.

Create API Key: https://console.groq.com/keys

#### `config.py`

```
GROQ_API_KEY = <GROQ_API_KEY>
```

### Tavily

Tavily is used for decentralized management and coordination of AI agents in multi-agent systems.

Create API Key: https://app.tavily.com/home

#### `config.py`

```
TAVILY_API_KEY = <TAVILY_API_KEY>
```

## Agents `agents.py`

This script holds the repository of agents required to solve the problem statement.

- `Router Agent`: Responsible for navigating the user query to either a vector store or web search based on relevance.
- `Retreiver Agent`: Resposnible for retrieving relevant information from the vector store to answer the user's question.
- `Grader Agent`: Responsible for evaluating the relevance of the retrieved documents to the user's question and filter out irrelevant ones.
- `Answer Grader Agent`: Responsible for assessing the final answer to ensure it is free from hallucinations.
- `Hallucination Grader Agent`: Responsible for identifying and filtering out any hallucinated or unsupported information in the answer.



