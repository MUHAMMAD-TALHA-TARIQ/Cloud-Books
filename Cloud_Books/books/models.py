from django.db import models
import uuid


class Books_Section(models.Model):
    parent_id = models.CharField(default="-", max_length=1000, blank=True, null=True)
    self_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    heading = models.CharField(max_length=100, default="", blank=True, null=True)
    paragraph = models.TextField(default="-", blank=True, null=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Book Sections"
