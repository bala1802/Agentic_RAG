"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai_tools  import tool

"""
Routes the given question to the appropriate tool based on its content.

This function determines which tool to use by analyzing the content of the question:
- If the question contains the term 'hindi' or 'marathi', it returns 'vectorstore'.
- For all other questions, it returns 'web_search'.
"""

@tool
def router_tool(question):
  
  """
  Args:
        question (str): The question or query that needs to be routed.

    Returns:
        str: The name of the tool to be used ('vectorstore' or 'web_search').
  """
  if 'hindi' in question or 'marathi' in question:
    return 'vectorstore'
  else:
    return 'web_search'