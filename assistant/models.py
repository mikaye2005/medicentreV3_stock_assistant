from django.db import models


class ConversationLog(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True)
    prompt_used = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ConversationLog #{self.id} - {self.created_at:%Y-%m-%d %H:%M:%S}"