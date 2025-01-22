from django.db import models

# Create your models here.

class AIResponse(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Response ({self.created_at}): {self.user_message[:50]}"
