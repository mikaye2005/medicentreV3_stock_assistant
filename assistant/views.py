from django.db import models
from django.db.models import F
from django.shortcuts import render

from .models import ConversationLog
from .services.answer_parser import parse_assistant_answer
from .services.ollama_client import OllamaClientError, chat_with_ollama
from .services.prompt_builder import build_stock_prompt
from legacydb.models import Tblitems, Tblitemstoragelocations, Tblstockchanges, Tblstocktakes


def build_dashboard_context():
    """
    Build dashboard numbers and short lists from the real stock database.
    """
    try:
        items_qs = Tblitems.objects.using("medicentre")
        storage_qs = Tblitemstoragelocations.objects.using("medicentre")
        changes_qs = Tblstockchanges.objects.using("medicentre")
        takes_qs = Tblstocktakes.objects.using("medicentre")

        total_items = items_qs.count()
        in_stock_count = storage_qs.filter(availablequantity__gt=0).count()
        low_stock_count = storage_qs.filter(
            reorderlevel__isnull=False,
            reorderlevel__gt=0,
            availablequantity__lte=F("reorderlevel"),
        ).count()
        out_of_stock_count = storage_qs.filter(availablequantity__lte=0).count()

        low_stock_alerts = list(
            storage_qs.filter(
                reorderlevel__isnull=False,
                reorderlevel__gt=0,
                availablequantity__lte=F("reorderlevel"),
            ).values(
                "itemstoragelocationid",
                "batch",
                "availablequantity",
                "reorderlevel",
            )[:5]
        )

        recent_stock_activity = list(
            changes_qs.order_by("-datetimechanged").values(
                "reference",
                "quantitychanged",
                "isincrement",
                "datetimechanged",
            )[:6]
        )

        total_stock_changes = changes_qs.count()
        total_stock_takes = takes_qs.count()

        return {
            "total_items": total_items,
            "in_stock_count": in_stock_count,
            "low_stock_count": low_stock_count,
            "out_of_stock_count": out_of_stock_count,
            "low_stock_alerts": low_stock_alerts,
            "recent_stock_activity": recent_stock_activity,
            "total_stock_changes": total_stock_changes,
            "total_stock_takes": total_stock_takes,
            "dashboard_error": None,
        }

    except Exception as exc:
        return {
            "total_items": 0,
            "in_stock_count": 0,
            "low_stock_count": 0,
            "out_of_stock_count": 0,
            "low_stock_alerts": [],
            "recent_stock_activity": [],
            "total_stock_changes": 0,
            "total_stock_takes": 0,
            "dashboard_error": str(exc),
        }


def test_ollama(request):
    question = ""
    answer = None
    error = None
    prompt_used = ""
    parsed_answer = {
        "direct_answer": "",
        "explanation": "",
        "relevant_tables": "",
        "raw_answer": "",
    }

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if not question:
            error = "Please type a question first."
        else:
            prompt_used = build_stock_prompt(question)

            try:
                answer = chat_with_ollama(prompt_used)
                parsed_answer = parse_assistant_answer(answer)

                ConversationLog.objects.create(
                    question=question,
                    answer=answer,
                    prompt_used=prompt_used,
                )

            except OllamaClientError as exc:
                error = str(exc)

    recent_logs = ConversationLog.objects.order_by("-created_at")[:5]

    context = {
        "question": question,
        "answer": answer,
        "parsed_answer": parsed_answer,
        "error": error,
        "prompt_used": prompt_used,
        "recent_logs": recent_logs,
    }
    context.update(build_dashboard_context())

    return render(request, "assistant/test_ollama.html", context)


def conversation_history(request):
    """
    Display saved conversation logs with optional search and date filtering.
    """
    logs = ConversationLog.objects.order_by("-created_at")

    query = request.GET.get("q", "").strip()
    date_value = request.GET.get("date", "").strip()

    if query:
        logs = logs.filter(
            models.Q(question__icontains=query) |
            models.Q(answer__icontains=query)
        )

    if date_value:
        logs = logs.filter(created_at__date=date_value)

    context = {
        "logs": logs,
        "search_query": query,
        "search_date": date_value,
    }
    context.update(build_dashboard_context())

    return render(request, "assistant/history.html", context)