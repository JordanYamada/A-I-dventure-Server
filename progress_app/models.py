from django.db import models
from django.core import validators as v
from story_app.models import Story
# from item_app.models import Item



# Create your models here.
class Progress(models.Model):

    title = models.CharField(
        blank=True,
        null=True,
    )
    
    image = models.CharField(
        blank=True,
        null=True,
    )

    decision = models.CharField(
        blank=True,
        null=True,
    )

    result = models.CharField(
        blank=True,
        null=True,
    )
    dialogue = models.CharField(
        blank=True,
        null=True,
    )
    epilogue = models.CharField(
        blank=True,
        null=True,
    )
    choice_one = models.CharField(
        blank=True,
        null=True,
    )
    danger_one = models.CharField(
        blank=True,
        null=True,
    )
    choice_two = models.CharField(
        blank=True,
        null=True,
    )
    danger_two = models.CharField(
        blank=True,
        null=True,
    )
    choice_three = models.CharField(
        blank=True,
        null=True,
    )
    danger_three = models.CharField(
        blank=True,
        null=True,
    )

    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null=True, related_name="progress")