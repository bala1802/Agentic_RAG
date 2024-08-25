"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai import Task
from crewai import Agent
from crewai_tools  import tool

"""
Initializes a Router Task responsible for analyzing a user's question and determining the appropriate search method.

This task is designed to:
- Analyze the keywords in a question provided by the user.
- Decide whether the question is eligible for a vectorstore search or a web search.
- Return a single word, either 'vectorstore' or 'websearch', based on the analysis.
- Avoid providing any preamble or explanation beyond the binary choice.

The task operates with the following characteristics:
- It is executed by the specified agent, which uses the provided tool to make the determination.
- The task is focused on returning a concise, binary output without any additional commentary.
"""

def initialize_router_task(agent: Agent, tool: tool):
    
    """
    Args:
        agent (Agent): The agent responsible for executing the task.
        tool (tool): The tool utilized by the agent to analyze the question and make the search method determination.

    Returns:
        Router_Task: An instance of the Task class configured to route questions to either a vectorstore search or a web search.
    """

    Router_Task = Task(
        description=("Analyse the keywords in the question {question}"
        "Based on the keywords decide whether it is eligible for a vectorstore search or a web search."
        "Return a single word 'vectorstore' if it is eligible for vectorstore search."
        "Return a single word 'websearch' if it is eligible for web search."
        "Do not provide any other premable or explaination."
        ),
        expected_output=("Give a binary choice 'websearch' or 'vectorstore' based on the question"
        "Do not provide any other premable or explaination."),
        agent=agent,
        tools=[tool],
    )

    return Router_Task

"""
Initializes a Retriever Task responsible for extracting information based on the response from a router task.

This task is designed to:
- Analyze the output from the router task to determine the appropriate tool for retrieving information.
- Use the web search tool if the router task output is 'websearch'.
- Use the RAG tool if the router task output is 'vectorstore'.
- Return a clear and concise text response based on the retrieved information.

The task operates with the following characteristics:
- It is executed by the specified agent, which uses the provided task to extract and retrieve the necessary information.
- The task's description and expected output guide how it should handle the response from the router task and utilize the 
appropriate tool.
"""
def initialize_retriever_task(agent: Agent, task: Task):
    """
    Args:
        agent (Agent): The agent responsible for executing the task.
        task (Task): The task that provides context and output from the router task.

    Returns:
        Retriever_Task: An instance of the Task class configured to retrieve and provide information based on the router task's 
        response.
    """
    Retriever_Task = Task(
        description=("Based on the response from the router task extract information for the question {question} with the help of the respective tool."
        "Use the web_serach_tool to retrieve information from the web in case the router task output is 'websearch'."
        "Use the rag_tool to retrieve information from the vectorstore in case the router task output is 'vectorstore'."
        ),
        expected_output=("You should analyse the output of the 'router_task'"
        "If the response is 'websearch' then use the web_search_tool to retrieve information from the web."
        "If the response is 'vectorstore' then use the rag_tool to retrieve information from the vectorstore."
        "Return a claer and consise text as response."),
        agent=agent,
        context=[task]
    )

    return Retriever_Task

"""
Initializes a Grader Task responsible for evaluating the relevance of retrieved content to a user's question.

This task is designed to:
- Evaluate whether the content retrieved by the retriever task is relevant to the question.
- Provide a binary score of 'yes' or 'no' based on the alignment of the retrieved content with the question asked.
- Return 'yes' if the retrieved content is relevant to the question and 'no' if it is not.

The task operates with the following characteristics:
- It is executed by the specified agent, which uses the provided task context to perform the evaluation.
- The task's description and expected output ensure that only a binary response is given, with no additional explanation or 
commentary.
"""
def initialize_grader_task(agent: Agent, task: Task):

    """
    Args:
        agent (Any): The agent responsible for executing the task.
        task (Any): The task that provides context and output from the retriever task for evaluation.

    Returns:
        Grader_Task: An instance of the Task class configured to evaluate and score the relevance of the retrieved content.
    """
    Grader_Task = Task(
        description=("Based on the response from the retriever task for the quetion {question} evaluate whether the retrieved content is relevant to the question."
        ),
        expected_output=("Binary score 'yes' or 'no' score to indicate whether the document is relevant to the question"
        "You must answer 'yes' if the response from the 'retriever_task' is in alignment with the question asked."
        "You must answer 'no' if the response from the 'retriever_task' is not in alignment with the question asked."
        "Do not provide any preamble or explanations except for 'yes' or 'no'."),
        agent=agent,
        context=[task],
    )

    return Grader_Task

"""
Initializes a Hallucination Task responsible for evaluating whether an answer is grounded in or supported by factual information.

This task is designed to:
- Assess whether the answer provided is grounded in factual information and is useful in the context of the question asked.
- Provide a binary score of 'yes' or 'no' based on the factual accuracy and relevance of the answer.
- Return 'yes' if the answer is useful and contains factual information about the question asked.
- Return 'no' if the answer is not useful and does not contain factual information about the question asked.

The task operates with the following characteristics:
- It is executed by the specified agent, using the provided task context to make the evaluation.
- The task's description and expected output ensure that only a binary response is provided, without any additional explanation.
"""
def initialize_hallucination_task(agent: Agent, task: Task):

    """
    Args:
        agent (Any): The agent responsible for executing the task.
        task (Any): The task that provides context and output from the grader task for evaluation.

    Returns:
        Hallucination_Task: An instance of the Task class configured to evaluate and score the factual grounding of the answer.
    """
    
    Hallucination_Task = Task(
        description=("Based on the response from the grader task for the quetion {question} evaluate whether the answer is grounded in / supported by a set of facts."),
        expected_output=("Binary score 'yes' or 'no' score to indicate whether the answer is sync with the question asked"
        "Respond 'yes' if the answer is in useful and contains fact about the question asked."
        "Respond 'no' if the answer is not useful and does not contains fact about the question asked."
        "Do not provide any preamble or explanations except for 'yes' or 'no'."),
        agent=agent,
        context=[task],
    )
    
    return Hallucination_Task

"""
Initializes an Answer Task responsible for providing a final response based on the evaluation of the answer's usefulness.

This task is designed to:
- Evaluate the response from the hallucination task to determine if the answer is useful in resolving the question.
- Return a clear and concise answer if the evaluation indicates the answer is useful.
- If the evaluation indicates the answer is not useful, perform a web search using 'web_search_tool' to find a better response.
- Return a default message if no valid response can be found.

The task operates with the following characteristics:
- It is executed by the specified agent, using the provided task context to generate or retrieve the appropriate response.
- The task's description and expected output guide how it should handle the result from the hallucination task and what actions to take based on that result.
"""
def initialize_answer_task(agent: Agent, task: Task):

    """
    Args:
        agent (Agent): The agent responsible for executing the task.
        task (Task): The task that provides context and output from the hallucination task for evaluation.

    Returns:
        Answer_Task: An instance of the Task class configured to provide a clear response based on the evaluation of the answer's usefulness.
    """
    Answer_Task = Task(
        description=("Based on the response from the hallucination task for the quetion {question} evaluate whether the answer is useful to resolve the question."
        "If the answer is 'yes' return a clear and concise answer."
        "If the answer is 'no' then perform a 'websearch' and return the response"),
        expected_output=("Return a clear and concise response if the response from 'hallucination_task' is 'yes'."
        "Perform a web search using 'web_search_tool' and return ta clear and concise response only if the response from 'hallucination_task' is 'no'."
        "Otherwise respond as 'Sorry! unable to find a valid response'."),
        context=[task],
        agent=agent
    )

    return Answer_Task