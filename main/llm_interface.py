"""
This module interacts with the Mistral language model via the local Ollama HTTP API.

Functions:
- ask_llm: Sends a question to the model and returns a generated response.
- ask_about_data: Formats a question using a pandas DataFrame and sends it to the model.
"""


import requests
import pandas as pd

def ask_llm(question: str) -> str: #
    """
       Args:
           question (str): The user’s question to send to the LLM.

       Returns:
           str: The LLM’s generated response text.
       """

    url = "http://localhost:11434/api/generate"

    payload = {"model": "mistral",
               "prompt": question,
               "stream": False
               }

    response = requests.post(url, json=payload)

    response.raise_for_status()
    result = response.json()

    return result['response']

def ask_about_data(df: pd.DataFrame, question: str) -> str:
    """
       Args:
           df (pd.DataFrame): The dataset to include in the prompt.
           question (str): The user's question about the dataset.

       Returns:
           str: The LLM's generated response based on the dataset.
       """


    data_str = df.to_string(index=False)

    prompt = (f"Here is a dataset: {data_str}. Based on this"
              f" data, please answer the following questions: {question}")

    return ask_llm(prompt)
