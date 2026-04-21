from django.contrib import admin

from .models import ConversationLog


@admin.register(ConversationLog)
class ConversationLogAdmin(admin.ModelAdmin):
    """
    Admin configuration for viewing saved assistant conversations.
    """

    list_display = ("id", "short_question", "created_at")
    search_fields = ("question", "answer")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    def short_question(self, obj):
        """
        Show a shortened version of the question in the admin list page.
        """
        return obj.question[:60] + "..." if len(obj.question) > 60 else obj.question

    short_question.short_description = "Question"