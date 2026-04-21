from django.urls import path
from .views import conversation_history, test_ollama

app_name = "assistant"

urlpatterns = [
    path("", test_ollama, name="test_ollama"),
    path("history/", conversation_history, name="conversation_history"),
]