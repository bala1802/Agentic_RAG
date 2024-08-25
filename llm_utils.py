"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from langchain_openai import ChatOpenAI
import os
import config

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
        openai_api_base=config.OPENAI_API_BASE,
        openai_api_key=os.environ['GROQ_API_KEY'],
        model_name=config.MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        max_tokens=config.LLM_MAX_TOKENS,
    )

    return llm