from django.contrib.auth import get_user_model
from django.db import models


class Card(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.IntegerField()
    credit = models.FloatField()
    solicitation_status = models.BooleanField(default=False)
