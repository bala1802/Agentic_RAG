"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai import Task
from crewai import Agent
from crewai_tools  import tool

import prompts as prompts

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
        description=(prompts.router_task_description),
        expected_output=(prompts.router_task_expected_outcome),
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
        description=(prompts.retreiver_task_description),
        expected_output=(prompts.retreiver_task_expected_outcome),
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
        description=(prompts.grader_task_description),
        expected_output=(prompts.grader_task_expected_outcome),
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
        description=(prompts.hallucination_task_description),
        expected_output=(prompts.hallucination_task_expected_outcome),
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
        description=(prompts.answer_task_description),
        expected_output=(prompts.answer_task_expected_outcome),
        context=[task],
        agent=agent
    )

    return Answer_Task