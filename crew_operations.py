"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai import Task
from crewai import Agent
from crewai import Crew

from typing import List

"""
Orchestrates a workflow by setting up a Crew with specified agents and tasks.

This function:
- Creates a `Crew` instance using the provided list of agents and tasks.
- Configures the `Crew` with verbose logging enabled for detailed output.
"""
def orchestrate_work_flow(agents: List[Agent], tasks: List[Task]):

    """
    Args:
        agents (List[Agent]): A list of `Agent` instances that will be part of the crew, each responsible for specific roles in the workflow.
        tasks (List[Task]): A list of `Task` instances that define the tasks to be managed and executed by the crew.

    Returns:
        rag_crew (Crew): An instance of the `Crew` class configured with the specified agents and tasks.
    """

    rag_crew = Crew(agents=agents, tasks=tasks, verbose=True)
    return rag_crew

"""
Executes the workflow managed by the given Crew instance using the specified inputs.

This function:
- Initiates the execution of the workflow by calling the `kickoff` method on the `Crew` instance.
- Passes the provided inputs to the `kickoff` method to drive the workflow execution.
"""
def execute_work_flow(rag_crew: Crew, inputs: dict):

    """
    Args:
        rag_crew (Crew): An instance of the `Crew` class responsible for managing and executing the workflow.
        inputs (Dict[str, str]): A dictionary of inputs required for the workflow execution. The keys are strings, and 
        the values can be of str type.

    Returns:
        result (str): The result of the workflow execution. The type of the result depends on the implementation of the `Crew` 
        class and its `kickoff` method.
    """

    result = rag_crew.kickoff(inputs=inputs)
    return result