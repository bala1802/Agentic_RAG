"""
Author: Balaguru Sivasambagupta
GitHub: https://github.com/bala1802
"""

from crewai_tools import PDFSearchTool

import requests
from typing import List

"""
Constructs a Retrieval-Augmented Generation (RAG) tool based on a given PDF URL.

This method performs the following tasks:
1. Downloads the PDF from the first URL in the provided list.
2. Saves the PDF locally as 'infosys_machine_translation.pdf'.
3. Initializes a RAG tool using the downloaded PDF and specific LLM and embedding model configurations.
"""

def construct_rag_tool(urls: List[str]):
    """
    Args:
        urls (List[str]): A list of URLs where the first URL is expected to point to a PDF file.

    Returns:
        rag_tool: An instance of the PDFSearchTool initialized with the downloaded PDF and configured models.
    """
    pdf_url = urls[0]
    response = requests.get(pdf_url)

    with open('infosys_machine_translation.pdf', 'wb') as file:
        file.write(response.content)
    
    rag_tool = PDFSearchTool(pdf='infosys_machine_translation.pdf',
    config=dict(
        llm=dict(
            provider="groq",
            config=dict(
                model="llama3-8b-8192"
            ),
        ),
        embedder=dict(
            provider="huggingface",
            config=dict(
                model="BAAI/bge-small-en-v1.5"
            ),
        ),
    )
)
    
    return rag_tool