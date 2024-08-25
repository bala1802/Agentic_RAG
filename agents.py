"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai import Agent
from langchain_openai import ChatOpenAI

"""
Initializes a Router Agent responsible for directing user questions to the appropriate service.

This agent routes questions to either a vectorstore or web search based on the content of the question:
- It uses a vectorstore for questions related to concepts in Retrieval-Augmented Generation (RAG).
- For all other types of questions, it uses web search.

The agent's behavior is controlled by the provided language model (LLM), and it operates under the following constraints:
- The agent will not delegate tasks.
- It will provide verbose output for better debugging and transparency.
"""
def initialize_router_agent(llm: ChatOpenAI):

    """
    Args:
        llm (ChatOpenAI): The language model used by the agent for decision-making.

    Returns:
        Router_Agent (Agent): An instance of the Agent class configured as a router.
    """

    Router_Agent = Agent(
        role='Router',
        goal='Route user question to a vectorstore or web search',
        backstory=(
            "You are an expert at routing a user question to a vectorstore or web search."
            "Use the vectorstore for questions on concept related to Retrieval-Augmented Generation."
            "You do not need to be stringent with the keywords in the question related to these topics. Otherwise, use web-search."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return Router_Agent

"""
Initializes a Retriever Agent responsible for answering questions using retrieved information from a vectorstore.

This agent is designed to:
- Assist with question-answering tasks.
- Utilize the information retrieved from the vectorstore to provide clear and concise answers to the user's questions.

The agent operates with the following characteristics:
- It acts as a dedicated assistant for question-answering.
- It does not delegate tasks to other agents.
- Verbose output is enabled to provide detailed feedback during its operations.
"""
def initialize_retriever_agent(llm: ChatOpenAI):

    """
    Args:
        llm (ChatOpenAI): The language model used by the agent for generating responses.

    Returns:
        Retriever_Agent (Agent): An instance of the Agent class configured as a retriever for question-answering tasks.
    """
    Retriever_Agent = Agent(
        role="Retriever",
        goal="Use the information retrieved from the vectorstore to answer the question",
        backstory=(
            "You are an assistant for question-answering tasks."
            "Use the information present in the retrieved context to answer the question."
            "You have to provide a clear concise answer."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return Retriever_Agent

"""
Initializes a Grader Agent responsible for evaluating the relevance of retrieved documents to a user question.

This agent is designed to:
- Assess the relevance of a document based on its content and the user's question.
- Grade the document as relevant if it contains keywords related to the question.
- Ensure that the answer aligns with the question, but without applying overly stringent criteria.

The agent operates with the following characteristics:
- It acts as a grader, focused on filtering out irrelevant or erroneous retrievals.
- It does not delegate tasks to other agents.
- Verbose output is enabled to provide detailed feedback during its operations.

"""
def initialize_grader_agent(llm: ChatOpenAI):

    """
    Args:
        llm (ChatOpenAI): The language model used by the agent for decision-making and grading.

    Returns:
        Grader_Agent (Agent): An instance of the Agent class configured as a grader for assessing document relevance.
    """
    Grader_Agent =  Agent(
        role='Answer Grader',
        goal='Filter out erroneous retrievals',
        backstory=(
            "You are a grader assessing relevance of a retrieved document to a user question."
            "If the document contains keywords related to the user question, grade it as relevant."
            "It does not need to be a stringent test.You have to make sure that the answer is relevant to the question."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return Grader_Agent


"""
Initializes a Hallucination Grader Agent responsible for evaluating whether an answer is grounded in factual information.

This agent is designed to:
- Assess the validity and grounding of an answer to ensure it aligns with the facts provided.
- Meticulously review the answer to ensure it is relevant and accurately responds to the question asked.
- Filter out any hallucinated information that is not supported by the given facts.

The agent operates with the following characteristics:
- It acts as a grader, focused on identifying and filtering out hallucinations in the responses.
- It does not delegate tasks to other agents.
- Verbose output is enabled to provide detailed feedback during its operations.
"""
def initialize_hallucination_grader_agent(llm: ChatOpenAI):

    """
    Args:
        llm (ChatOpenAI): The language model used by the agent for decision-making and grading the responses.

    Returns:
        Hallucination_Grader_Agent (Agent): An instance of the Agent class configured to assess and filter out hallucinated 
        information in answers.
    """

    Hallucination_Grader_Agent = Agent(
        role="Hallucination Grader",
        goal="Filter out hallucination",
        backstory=(
            "You are a hallucination grader assessing whether an answer is grounded in / supported by a set of facts."
            "Make sure you meticulously review the answer and check if the response provided is in alignmnet with the question asked"
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return Hallucination_Grader_Agent

"""
Initializes an Answer Grader Agent responsible for evaluating the relevance and accuracy of answers.

This agent is designed to:
- Assess whether an answer is useful in resolving the question posed by the user.
- Meticulously review the answer to ensure it makes sense and is aligned with the question asked.
- If the answer is relevant, the agent generates a clear and concise response.
- If the answer is not relevant, the agent initiates a web search using the 'web_search_tool' to find the correct information.

The agent operates with the following characteristics:
- It acts as a grader, focused on filtering out hallucinations and irrelevant information from answers.
- It does not delegate tasks to other agents.
- Verbose output is enabled to provide detailed feedback during its operations.
"""
def initialize_answer_grader_agent(llm: ChatOpenAI):

    """
    Args:
        llm (ChatOpenAI): The language model used by the agent for decision-making and grading the responses.

    Returns:
        Answer_Grader_Agent: An instance of the Agent class configured to assess and filter answers, 
        ensuring they are relevant and accurate.
    """
    Answer_Grader_Agent = Agent(
        role="Answer Grader",
        goal="Filter out hallucination from the answer.",
        backstory=(
            "You are a grader assessing whether an answer is useful to resolve a question."
            "Make sure you meticulously review the answer and check if it makes sense for the question asked"
            "If the answer is relevant generate a clear and concise response."
            "If the answer gnerated is not relevant then perform a websearch using 'web_search_tool'"
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return Answer_Grader_Agent