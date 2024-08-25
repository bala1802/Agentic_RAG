"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from langchain_openai import ChatOpenAI
import os

from config import OPENAI_API_BASE
from config import LLM_MAX_TOKENS
from config import MODEL_NAME
from config import LLM_TEMPERATURE

"""
Initializes and configures an instance of the ChatOpenAI language model.

This function:
- Creates and configures an instance of ChatOpenAI with parameters defined in the config module and environment variables.
- Sets up the API base URL, API key, model name, temperature, and maximum tokens for the language model.
"""
def initialize_llm() -> ChatOpenAI:
    
    """
    Returns:
        llm (Any): An instance of ChatOpenAI configured with the specified parameters.
    """

    llm = ChatOpenAI(
        openai_api_base=OPENAI_API_BASE,
        openai_api_key=os.environ['GROQ_API_KEY'],
        model_name=MODEL_NAME,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS,
    )

    return llm