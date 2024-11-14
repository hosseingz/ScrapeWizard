import requests
import ollama


def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True, response.text

    except requests.exceptions.HTTPError as http_err:
        return False, f"HTTP error occurred: {http_err}"  # HTTP error
    except requests.exceptions.ConnectionError as conn_err:
        return False, f"Connection error occurred: {conn_err}"  # Connection error
    except requests.exceptions.Timeout as timeout_err:
        return False, f"Timeout error occurred: {timeout_err}"  # Timeout error
    except requests.exceptions.RequestException as req_err:
        return False, f"An error occurred: {req_err}"  # Other errors
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"  # Unexpected error


def ask_ai(user_prompt):
    stream = ollama.chat(
        model='phi3:mini',
        messages=[
            {'role': 'user', 'content': f"{user_prompt}"}
            ],
        stream=True,
    )

    return stream



def stream_parser(stream):
    for chunk in stream:
        yield chunk['message']['content']