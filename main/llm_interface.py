import os
import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Fetch the URL of Ollama from the environment variable, defaulting to localhost for local development
ollama_url = os.getenv('OLLAMA_URL', 'http://localhost:11434')

def ask_llm(question: str) -> str:
    """
       Args:
           question (str): The user’s question to send to the LLM.

       Returns:
           str: The LLM’s generated response text.
       """
    # Use the dynamic Ollama URL
    url = f"{ollama_url}/api/generate"
    payload = {"model": "mistral:7b", "prompt": question, "stream": False}

    try:
        # Attempt to send the request to the LLM API
        response = requests.post(url, json=payload)

        # Check if the response is successful (status code 200)
        response.raise_for_status()

        # If the request is successful, parse the JSON response
        result = response.json()
        return result.get('response', "No response found in the LLM's output.")

    except requests.exceptions.HTTPError as http_err:
        # Catch HTTP errors (e.g., 404, 500)
        logging.error(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
        return f"HTTP error occurred: {http_err} - Status Code: {response.status_code}"

    except requests.exceptions.ConnectionError as conn_err:
        # Catch connection errors (e.g., network issues, server unreachable)
        logging.error(f"Connection error occurred: {conn_err}")
        return f"Connection error occurred: {conn_err}"

    except requests.exceptions.Timeout as timeout_err:
        # Catch timeout errors (e.g., request timeout)
        logging.error(f"Timeout error occurred: {timeout_err}")
        return f"Timeout error occurred: {timeout_err}"

    except requests.exceptions.RequestException as req_err:
        # Catch any general request errors
        logging.error(f"An error occurred during the request: {req_err}")
        return f"An error occurred during the request: {req_err}"

    except Exception as e:
        # Catch any other exceptions that may occur
        logging.error(f"Unexpected error: {e}")
        return f"Unexpected error: {e}"

def ask_about_data(df: pd.DataFrame, question: str) -> str:
    """
       Args:
           df (pd.DataFrame): The dataset to include in the prompt.
           question (str): The user's question about the dataset.

       Returns:
           str: The LLM's generated response based on the dataset.
       """
    try:
        data_str = df.to_string(index=False)

        prompt = f"Here is a dataset: {data_str}. Based on this data, please answer the following questions: {question}"

        return ask_llm(prompt)

    except Exception as e:
        logging.error(f"Error in processing the dataset or question: {e}")
        return f"Error in processing the dataset or question: {e}"
