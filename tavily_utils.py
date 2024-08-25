"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from langchain_community.tools.tavily_search import TavilySearchResults
from config import NUMBER_OF_WEB_SEARCH_RESULTS

def initialize_web_search_tool():
    web_search_tool = TavilySearchResults(k=NUMBER_OF_WEB_SEARCH_RESULTS)
    return web_search_tool