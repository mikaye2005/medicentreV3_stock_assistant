from .stock_context import STOCK_SCHEMA_CONTEXT
from .db_context import build_live_stock_context
from .fact_builder import build_controlled_stock_facts


def build_stock_prompt(user_question: str) -> str:
    """
    Build the final prompt for the stock assistant.

    This combines:
    - schema understanding from our investigation
    - live database summary chosen according to the user question
    - controlled stock facts from the real database
    - the user question itself
    """
    live_context = build_live_stock_context(user_question)
    controlled_facts = build_controlled_stock_facts(user_question)

    return f"""
You are a stock-focused AI assistant for MedicentreV3.

Use the stock schema context, live database summary, and verified stock facts below to answer the user's question.

Stock schema context:
{STOCK_SCHEMA_CONTEXT}

Live database summary:
{live_context}

Verified stock facts:
{controlled_facts}

User question:
{user_question}

Instructions:
- Answer only from the stock context provided.
- Use the verified stock facts as the highest-priority factual source.
- Use simple and professional language.
- Mention table names when necessary.
- If something is uncertain, say so clearly.
- Do not invent tables, columns, or workflow details.
- Do not use markdown symbols like ** unless necessary.
- Your response must follow this exact format:

Direct Answer: <one clear sentence>

Explanation: <2 to 4 clear sentences>

Relevant Table(s): <table names only, separated by commas>
""".strip()