import requests
from django.conf import settings


class OllamaClientError(Exception):
    """Raised when Ollama cannot be reached or returns a bad response."""
    pass


def chat_with_ollama(user_message: str) -> str:
    """
    Send one user message to Ollama and return the model's text reply.
    """
    payload = {
        "model": settings.OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "stream": False,
    }

    try:
        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/chat",
            json=payload,
            timeout=(5, 120),
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise OllamaClientError(f"Could not reach Ollama: {exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise OllamaClientError("Ollama returned invalid JSON.") from exc

    content = data.get("message", {}).get("content", "").strip()

    if not content:
        raise OllamaClientError("Ollama returned an empty response.")

    return content